const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Раздаем статику (HTML, CSS, JS)
app.use(express.static(path.join(__dirname, 'public')));

// API для проверки
app.get('/api', (req, res) => {
    res.json({ message: 'API работает!' });
});

// Запуск сервера
app.listen(PORT, () => {
    console.log(`Сервер запущен на http://localhost:${PORT}`);
});