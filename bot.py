import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

# Вставьте сюда токен от @BotFather (вместо этого примера)
TOKEN = "9060701165:AAHLDalbbCat502cl10A6QAyk4RAkHUl6hM"

dp = Dispatcher()

START_TEXT = (
    "🎮 Этот бот приватный.\n\n"
    "Чтобы получить доступ, отправьте 100 звёзд на юзернейм @MarketRedo_Buyer\n\n"
    "😄 Шутка, ничего отправлять не нужно!"
)


@dp.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(START_TEXT)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
