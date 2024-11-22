from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import os

# Токен вашего бота
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Переменная окружения для токена

if not BOT_TOKEN:
    raise ValueError("Токен бота не найден. Проверьте переменные окружения Render.")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Бот успешно работает на Render.")

if __name__ == "__main__":
    executor.start_polling(dp)