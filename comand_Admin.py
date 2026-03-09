from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router_admin = Router()

@router_admin.message(Command('Admin'))
async def start(message: Message):
    await message.reply(
        "Вы нажали на кнопку Admin",

    )