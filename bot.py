import logging

from aiogram import Bot, Dispatcher,executor, types

API_TOKEN = '6456617315:AAGixsiR4jaG7z3DXLNF8SPge0UEOJ6G1BQ'

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token="6456617315:AAGixsiR4jaG7z3DXLNF8SPge0UEOJ6G1BQ")

# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(Command=["start","help"])
async def cmd_start(message: types.Message):

    await message.answer("hello! xushgalding bro .!")

# Запуск процесса поллинга новых апдейтов

@dp.message_handler()
async def echo (massege :types.Messege):
    await message.answer(message.text)


if __name__ == "__main__":
    asyncio.run(main())