import json
import os
import time
import requests

BASE_URL = os.environ["BASE_URL"].rstrip("/")
EMAIL = os.environ["ADMIN_EMAIL"]
PASSWORD = os.environ["ADMIN_PASSWORD"]

LABEL_MAP = {
    "area:psychology":     "lavender-fields",
    "area:marketing":      "pumpkin-orange",
    "area:design":         "lagoon-blue",
    "area:implementation": "modern-green",
    "type:note":           "morning-sky",
    "type:experiment":     "egg-yellow",
    "type:review":         "pink-tulip",
    "priority:high":       "apricot-red",
    "priority:medium":     "light-orange",
    "priority:low":        "sunny-grass",
}


def get_token(session):
    r = session.post(f"{BASE_URL}/api/access-tokens", json={
        "emailOrUsername": EMAIL,
        "password": PASSWORD,
    })
    data = r.json()

    if data.get("step") == "accept-terms":
        pending_token = data["pendingToken"]
        terms = session.get(f"{BASE_URL}/api/terms").json()
        signature = terms["item"]["signature"]
        r2 = session.post(f"{BASE_URL}/api/access-tokens/accept-terms", json={
            "pendingToken": pending_token,
            "signature": signature,
        })
        r2.raise_for_status()
        item = r2.json()["item"]
        return item if isinstance(item, str) else item["token"]

    r.raise_for_status()
    item = data["item"]
    return item if isinstance(item, str) else item["token"]


def create_project(session, name):
    r = session.post(f"{BASE_URL}/api/projects", json={"name": name, "type": "private"})
    r.raise_for_status()
    return r.json()["item"]


def create_board(session, project_id, name, position):
    r = session.post(f"{BASE_URL}/api/projects/{project_id}/boards", json={
        "name": name,
        "position": position,
    })
    r.raise_for_status()
    return r.json()["item"]


def create_list(session, board_id, name, position):
    r = session.post(f"{BASE_URL}/api/boards/{board_id}/lists", json={
        "name": name,
        "position": position,
        "type": "active",
    })
    r.raise_for_status()
    return r.json()["item"]


def create_label(session, board_id, name, color, position):
    r = session.post(f"{BASE_URL}/api/boards/{board_id}/labels", json={
        "name": name,
        "color": color,
        "position": position,
    })
    if not r.ok:
        print(f"  Label error: {r.status_code} {r.text[:200]}")
    r.raise_for_status()
    return r.json()["item"]


def create_card(session, list_id, name, description, position):
    r = session.post(f"{BASE_URL}/api/lists/{list_id}/cards", json={
        "name": name,
        "description": description or None,
        "position": position,
        "type": "story",
    })
    r.raise_for_status()
    return r.json()["item"]


def add_label_to_card(session, card_id, label_id):
    r = session.post(f"{BASE_URL}/api/cards/{card_id}/card-labels", json={
        "labelId": label_id,
    })
    r.raise_for_status()


def main():
    issues_path = os.path.join(os.path.dirname(__file__), "issues.json")
    with open(issues_path) as f:
        issues = json.load(f)
    issues = sorted(issues, key=lambda x: x["number"])

    session = requests.Session()
    token = get_token(session)
    session.headers.update({"Authorization": f"Bearer {token}"})
    print("Authenticated.")

    project = create_project(session, "Behavioral Design Engineer Roadmap")
    print(f"Project created: {project['id']}")

    board = create_board(session, project["id"], "Roadmap", 65535)
    print(f"Board created: {board['id']}")

    todo_list  = create_list(session, board["id"], "To Do",       65535)
    inprogress = create_list(session, board["id"], "In Progress", 131071)
    done_list  = create_list(session, board["id"], "Done",        196607)
    print("Lists created.")

    created_labels = {}
    pos = 65535
    for gh_label, color in LABEL_MAP.items():
        label = create_label(session, board["id"], gh_label, color, pos)
        created_labels[gh_label] = label["id"]
        pos += 65535
    print(f"Labels created: {len(created_labels)}")

    for i, issue in enumerate(issues):
        pos = (i + 1) * 65535
        card = create_card(
            session,
            todo_list["id"],
            issue["title"],
            issue.get("body") or "",
            pos,
        )
        print(f"  Card #{issue['number']}: {issue['title'][:50]}")

        for gh_label in issue.get("labels", []):
            if gh_label in created_labels:
                add_label_to_card(session, card["id"], created_labels[gh_label])

        time.sleep(0.1)

    print(f"\nMigration complete. Open {BASE_URL}")


if __name__ == "__main__":
    main()
