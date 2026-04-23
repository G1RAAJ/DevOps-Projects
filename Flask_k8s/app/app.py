from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body { font-family: Arial; background:#f4f4f4; text-align:center; padding-top:80px; }
            .box { background:white; padding:25px; border-radius:8px; display:inline-block; }
            input { display:block; margin:10px auto; padding:8px; width:200px; }
            a { font-size:12px; }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Flask Application</h2>
            <input type="text" placeholder="Login Name">
            <input type="password" placeholder="Password">
            <a href="#">Forgot Password?</a>
            <p style="margin-top:15px; color:green;">
                ✔ Application running successfully
            </p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
