from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from reply import klavish
router_start = Router()

@router_start.message(Command('StartQuiz'))
async def start(message: Message):
    await message.reply(
        "👋 Добро пожаловать в EnglishQuizBot\n"
        "Этот бот помогает улучшить ваш словарь на английском.",
        reply_markup=klavish
    )