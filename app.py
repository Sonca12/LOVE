from flask import Flask, render_template, request

app = Flask(__name__)

# Lưu tin nhắn từ người dùng
messages = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        msg = request.form.get("message")
        if msg:
            messages.append(msg)
    return render_template("index.html", messages=messages)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Dùng cổng Render cấp hoặc mặc định là 5000
    app.run(host="0.0.0.0", port=port)


 
