import asyncio
import os
from dotenv import load_dotenv
from  aiogram import Bot,Dispatcher
from aiogram.types import Message,FSInputFile
from aiogram.filters import Command

load_dotenv()

Token = os.getenv("Token")

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_command(message: Message):
    await message.answer_photo(
        photo=FSInputFile("eng2.png"),
        caption="Привет я EnglishQuizBot,если хочешь узнать поподробнее то нажми на /help"
    )
@dp.message(Command('help'))
async def help_command(message: Message):
    await message.answer_photo(
        photo=FSInputFile("./eng.png"),
        caption="Я бот про английского викторины, с помощью меня ты сможешь улучшить свой английский и память"

    )
@dp.message(Command('about_bot'))
async def about_bot_command(message: Message):
    await message.answer_photo(
        photo=FSInputFile("./eng.png"),
        caption="Я был создан в Бишкеке \nУ вас наверное есть вопросы Зачем меня создали?\n"
        "Я нужен для того чтобы люди начали хоть немного разговаривать на английском"

    )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())













