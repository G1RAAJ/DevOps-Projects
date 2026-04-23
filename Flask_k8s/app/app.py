from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background-color: #f4f4f4;
                padding-top: 100px;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.2);
                display: inline-block;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask App Running</h1>
            <p>Deployed via Kubernetes CI/CD Pipeline</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
