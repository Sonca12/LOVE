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



from flask import Flask, render_template, request, redirect, flash
import smtplib

app = Flask(__name__)
app.secret_key = "tung2004"  # Thêm khóa bí mật để sử dụng flash messages.

# Danh sách mục tiêu
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

# Route chính
@app.route("/")
def home():
    return render_template("index.html")

# Route hiển thị mục tiêu
@app.route("/goals")
def goals_page():
    return render_template("goals.html", goals=goals)

# Hàm gửi email
def send_email(subject, message, to_email):
    sender_email = "bachquangtung162@gmail.com"
    sender_password = "bbfk hsqq jnad xtgw"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        # Kết nối tới server SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Gửi email
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, to_email, email_message)
        server.quit()
        print("Email đã được gửi thành công!")
    except Exception as e:
        print(f"Không thể gửi email: {e}")

# Route xử lý khi nhấn nút "Gửi"
@app.route("/send-goal", methods=["POST"])
def send_goal():
    # Lấy dữ liệu từ form
    month = request.form.get("month")
    goal = request.form.get("goal")

    # Gửi email tới bạn và người yêu
    subject = f"Mục tiêu tháng {month}"
    message = f"Chào em,\n\nMục tiêu tháng {month} của chúng mình  là: {goal}\n\nChúc we hoàn thành xuất sắc mục tiêu này!"
    send_email(subject, message, "your_email@gmail.com")  # Thay email của bạn
    send_email(subject, message, "friend_email@gmail.com")  # Thay email của người yêu

    # Hiển thị thông báo
    flash(f"Mục tiêu tháng {month} đã được gửi thành công!")
    return redirect("/goals")

if __name__ == "__main__":
    app.run(debug=True)

