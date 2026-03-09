from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router_mystats = Router()

@router_mystats.message(Command('MyStats'))
async def start(message: Message):
    await message.reply(
        "Вот ваша статистика ",

    )