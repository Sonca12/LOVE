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


 
from flask import Flask, render_template

app = Flask(__name__)

goals = {
    3: "Đón sinh nhật cùng anh",
    4: "Đón sinh nhật cùng em và cả 2 có bằng lái",
    5: "Đón tròn 1 năm yêu nhau ở Phan Thiết",
    6: "Đi cắm trại cùng nhau, hạnh phúc bên nhau",
    7: "Làm một điều bất ngờ cho người yêu",
    8: "Lên kế hoạch cho sinh nhật",
    9: "Tổ chức buổi hẹn hò đặc biệt",
    10: "Tham gia một lớp học cùng nhau",
    11: "Dọn dẹp và trang trí lại phòng",
    12: "Tổng kết năm và viết lời chúc cho năm mới",
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/goals")
def goals_page():
    return render_template("goals.html", goals=goals)

if __name__ == "__main__":
    app.run(debug=True)
