console.log("Trang web tình yêu đã sẵn sàng! 💕");

// Hiệu ứng đổi màu tiêu đề sau mỗi 2 giây
setInterval(() => {
    const title = document.querySelector("h1");
    title.style.color = title.style.color === "red" ? "#ff1493" : "red";
}, 2000);
function checkQuiz() {
    let answer1 = document.getElementById("answer1").value.toLowerCase();
    let answer2 = document.getElementById("answer2").value;
    
    if (answer1.includes("lần đầu hẹn hò") && answer2 === "duong") {
        document.getElementById("quiz-result").innerText = "Bạn hiểu nhau thật đấy! 💕";
    } else {
        document.getElementById("quiz-result").innerText = "Hmmm, có vẻ cần nhớ lại kỷ niệm rồi! 😆";
    }
}
function getRandomChallenge() {
    let challenges = [
        "Hôn người yêu ngay bây giờ! 💋",
        "Nhắn tin 3 điều bạn yêu nhất ở đối phương 💌",
        "Chụp ngay một bức ảnh đôi và lưu lại! 📸",
        "Cùng nhau hát một bài hát tình yêu 🎶",
        "Kể một kỷ niệm đẹp nhất mà bạn nhớ về người kia 💖"
    ];
    let randomIndex = Math.floor(Math.random() * challenges.length);
    document.getElementById("challenge-result").innerText = challenges[randomIndex];
}
 
