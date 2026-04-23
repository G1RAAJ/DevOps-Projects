from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <html>
    <head>
        <title>Flask Dashboard</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .container {{
                text-align: center;
                background: #1e293b;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0,0,0,0.5);
            }}
            h1 {{
                color: #38bdf8;
            }}
            .status {{
                margin-top: 20px;
                font-size: 18px;
                color: #22c55e;
            }}
            .time {{
                margin-top: 10px;
                font-size: 14px;
                color: #cbd5f5;
            }}
            button {{
                margin-top: 25px;
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                background: #38bdf8;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }}
            button:hover {{
                background: #0ea5e9;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask CI/CD Dashboard</h1>
            <div class="status">✔ Application Running Successfully</div>
            <div class="time">Last refreshed: {now}</div>
            <button onclick="location.reload()">Refresh</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
