from aiogram import Bot, Dispatcher
import asyncio
from app.handlers import router
from config import TOKEN
import logging




bot = Bot(TOKEN)
dp = Dispatcher()



async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit!')
        