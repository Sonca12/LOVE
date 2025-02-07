from datetime import datetime
import smtplib

goals = {
    3: "Đón sinh nhật cùng anh ",
    4: "Đón sinh nhật cùng em và cả 2 có bằng lái  ",
    5: "Đón tròn 1 năm yêu nhau ở phan thiết",
    6: "Đi cắm trại cùng nhau hpan cùng nhau",
    7: "vẽ tranh cùng nhau",
    8: "ráp logo cùng nhau",
    9: "Tặng trang sức cùng nhau",
    10: "Đi du lịch cùng nhau",
    11: "Làm album ảnh cùng nhau",
    12: "Tổng kết năm và viết lời chúc cho năm mới",
}

def send_email(subject, message, to_email):
    sender_email = "bachquangtung162@gmail.com@gmail.com"
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

    if current_month in goals:
        subject = "Nhắc nhở hoàn thành mục tiêu tháng"
        message = f"EM ƠI MỤC TIÊU THÁNG NÀY CHƯA ĐƯỢC HOÀN THÀNH BẠN TRANH THỦ HOÀN THÀNH NHÉ\n\nMục tiêu: {goals[current_month]}"
        send_email(subject, message, "bachquangtung162@gmail.com")
        send_email(subject, message, "nguyenlethuyduong99@gmail.com")

if __name__ == "__main__":
    check_goals()
 
