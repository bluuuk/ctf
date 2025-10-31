import typing

from flask import Flask, request
from jinja2.sandbox import SandboxedEnvironment

app = Flask(__file__)

env = SandboxedEnvironment()
env.globals["typing"] = typing


@app.post("/")
def render():
    content = request.form["content"]
    print(content)
    if "module" in content:
        return "funny abuser."
    # 😇😇😇
    try:
        assert len(content) < 75
        return env.from_string(content).render()
    except Exception as e:
        import traceback
        return traceback.format_exc()
        # 🚨🚨🚨
        return "funny user."


if __name__ == "__main__":
    app.run("0.0.0.0", 1337, debug=False)
