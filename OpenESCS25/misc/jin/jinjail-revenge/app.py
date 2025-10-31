import typing

from flask import Flask, request
from jinja2.sandbox import SandboxedEnvironment

app = Flask(__file__)

env = SandboxedEnvironment()
env.globals["typing"] = typing


@app.post("/")
def render():
    content = request.form["content"]
    if "module" in content:
        return "funny (ab)user."
    # 😇😇😇
    try:
        assert len(content) < 75
        return env.from_string(content).render()
    except:
        # 🚨🚨🚨
        return "funny (ab)user."


if __name__ == "__main__":
    app.run("0.0.0.0", 1337, debug=False)
