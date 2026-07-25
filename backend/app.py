from flask import Flask, render_template
from datetime import datetime
import os
import socket

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "Hello Docker World")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")


@app.route("/")
def home():
    hostname = socket.gethostname()
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_version=APP_VERSION,
        environment=ENVIRONMENT,
        hostname=hostname,
        now=now,
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)