import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("9060701165:AAHLDalbbCat502cl10A6QAyk4RAkHUl6hM")
if not TOKEN:
    raise RuntimeError("Не задан BOT_TOKEN. Укажите токен в переменной окружения.")

dp = Dispatcher()

START_TEXT = (
    "🎮 Этот бот приватный.\n\n"
    "Чтобы получить доступ, отправьте 100 звёзд на юзернейм @MarketRedo_Buyer. Сразу после оплаты напишите /start"
)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(START_TEXT)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
