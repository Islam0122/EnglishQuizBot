import asyncio
from aiogram import Bot, Dispatcher, types
from config import Config, load_config
from comand_Start import router_start
from comand_MyStats import router_mystats
from comand_Admin import router_admin

async def main() -> None:
    config: Config = load_config()
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    dp.include_router(router_start)
    dp.include_router(router_mystats)
    dp.include_router(router_admin)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())











