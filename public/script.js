const tg = window.Telegram.WebApp;

// Обрабатываем нажатие кнопки
document.getElementById('sendData').addEventListener('click', () => {
    const user = tg.initDataUnsafe.user || { username: "Unknown" };
    tg.sendData(`Привет, ${user.username}!`); // Отправляем данные боту
});

// Разворачиваем WebApp на весь экран
tg.expand();