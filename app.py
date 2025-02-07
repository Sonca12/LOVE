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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # Chạy trên localhost
 
