import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# Подгружаем переменные из .env
from dotenv import load_dotenv
load_dotenv()

# Получаем токен бота из .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверка: если токен отсутствует
if not BOT_TOKEN:
    raise ValueError("Токен бота не найден. Убедитесь, что он указан в файле .env.")

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Создаем кнопку с WebApp
    keyboard = InlineKeyboardMarkup()
    webapp_button = InlineKeyboardButton(
        text="Открыть WebApp",
        web_app=types.WebAppInfo(url="https://your-webapp-url.com")  # Замените на ваш URL
    )
    keyboard.add(webapp_button)
    await message.answer("Нажмите на кнопку ниже, чтобы открыть WebApp:", reply_markup=keyboard)

if __name__ == "__main__":
    executor.start_polling(dp)