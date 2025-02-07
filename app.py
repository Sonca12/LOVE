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
from datetime import datetime
import smtplib

app = Flask(__name__)

# Danh sách mục tiêu của 12 tháng
goals = {
    3: "Đón sinh nhật cùng anh ",
    4: "Đón sinh nhật cùng em và cả 2 có bằng lái  ",
    5: "Đón tròn 1 năm yêu nhau ở phan thiết",
    6: "Đi cắm trại cùng nhau hpan cùng nhau",
    7: "Mua đồ đôi cùng nhau", 
    8: "Tặng trang sức cho nhau",
    9: "Xếp 1 logo to cùng nhau",
    10: "Vẽ tranh cùng nhau",
    11: "Làm album ảnh cùng nhau",
    12: "Tổng kết năm và viết lời chúc cho năm mới"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/goals")
def goals_page():
    return render_template("goals.html", goals=goals)

if __name__ == "__main__":
    app.run(debug=True)

def send_email(subject, message, to_email):
    # Cấu hình email của bạn
    sender_email = "bachquangtung162@gmail.com"
    sender_password = "bbfk hsqq jnad xtgw"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, to_email, email_message)
        server.quit()
        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Không thể gửi email: {e}")


def check_goals():
    today = datetime.now()
    current_month = today.month

    # Thông điệp email
    subject = "Nhắc nhở hoàn thành mục tiêu tháng"
    message = f"EM ƠI MỤC TIÊU THÁNG NÀY CHƯA ĐƯỢC HOÀN THÀNH BẠN TRANH THỦ HOÀN THÀNH NHÉ\n\nMục tiêu: {goals[current_month]}"
    
    # Gửi email cho bạn và người yêu
    send_email(subject, message, "bachquangtung162@gmail.com")  # Email của bạn
    send_email(subject, message, "nguyenlethuyduong99@gmail.com")  # Email của người yêu

import schedule
import time

# Lịch chạy: Gửi email vào giữa tháng (ngày 15) và cuối tháng (ngày 28)
schedule.every().month.at("15:00").do(check_goals)

while True:
    schedule.run_pending()
    time.sleep(1)

