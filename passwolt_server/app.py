"""
Passwolt storage backend server

The encrypted passwords are stored in here.
"""

import json
import logging
import os

from flask import Flask, request
from passwolt_server.util import SERVER_CONFIG_PATH


app = Flask("passwolt-server")


def disable_flask_logging():
    os.environ["WERKZEUG_RUN_MAIN"] = "true"
    log = logging.getLogger("werkzeug")
    log.setLevel(logging.ERROR)


def run():
    disable_flask_logging()
    with open(SERVER_CONFIG_PATH, "r") as f:
        data = json.load(f)
        app._passwolt_db_path = data["path"]
        host = data["host"]
        port = data["port"]
    app.run(host=host, port=port)


@app.route("/get", methods=["POST"])
def get_db():
    with open(app._passwolt_db_path, "r") as f:
        return f.read(), 200


@app.route("/set", methods=["POST"])
def set_db():
    data = request.form.get("data")
    if not data:
        return "Data missing", 400
    with open(app._passwolt_db_path, "w") as f:
        f.write(data)
    return "OK", 200
