from flask import Flask
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

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{APP_NAME}</title>
        <style>
            body {{
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                background: linear-gradient(135deg, #1e293b, #0f172a);
                color: #f1f5f9;
            }}
            .card {{
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 48px 56px;
                text-align: center;
                box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
                backdrop-filter: blur(6px);
            }}
            h1 {{
                margin: 0 0 8px;
                font-size: 2.2rem;
                background: linear-gradient(90deg, #38bdf8, #818cf8);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}
            p.tag {{
                margin: 0 0 28px;
                color: #94a3b8;
                font-size: 0.95rem;
            }}
            .meta {{
                display: grid;
                grid-template-columns: auto auto;
                gap: 6px 16px;
                text-align: left;
                font-size: 0.9rem;
                color: #cbd5e1;
            }}
            .meta span.label {{
                color: #64748b;
            }}
            .badge {{
                display: inline-block;
                margin-top: 24px;
                padding: 4px 12px;
                border-radius: 999px;
                background: rgba(56, 189, 248, 0.15);
                color: #38bdf8;
                font-size: 0.8rem;
                font-weight: 600;
                letter-spacing: 0.03em;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{APP_NAME}</h1>
            <p class="tag">Shipped via Docker; deployed CI/CD Github Actions 🚀</p>
            <div class="meta">
                <span class="label">Version</span><span>{APP_VERSION}</span>
                <span class="label">Environment</span><span>{ENVIRONMENT}</span>
                <span class="label">Hostname</span><span>{hostname}</span>
                <span class="label">Server time</span><span>{now}</span>
            </div>
            <div class="badge">● running</div>
        </div>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)