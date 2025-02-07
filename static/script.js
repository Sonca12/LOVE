console.log("Trang web tình yêu đã sẵn sàng! 💕");

// Hiệu ứng đổi màu tiêu đề sau mỗi 2 giây
setInterval(() => {
    const title = document.querySelector("h1");
    title.style.color = title.style.color === "red" ? "#ff1493" : "red";
}, 2000);
 
