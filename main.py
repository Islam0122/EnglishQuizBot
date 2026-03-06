import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot,Dispatcher
from aiogram.types import Message,FSInputFile
from aiogram.filters import Command

load_dotenv()

TOKEN = os.getenv("Token")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: Message):
    await (message.answer("Привет я бот EnglishQuizBot"))

@dp.message(Command('help'))
async def helper(message: Message):
    await (message.answer("Я могу помочь что ты хочешь мне задать вопрос"))
    await (message.answer_photo(
        photo=FSInputFile("photo/Helperit_photo.png"),
        caption="Только так я могу тебе помочь",))


@dp.message(Command('about_bot'))
async def about_bot(message: Message):
    await message.answer_photo(
        photo=FSInputFile("photo/Test_anglish.png"),
        caption="Тесты буду на английском языке и вы научитесь новым словам и грамматике!!",

    )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())