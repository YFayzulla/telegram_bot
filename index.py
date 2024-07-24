import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import executor
from aiogram.types import ParseMode

API_TOKEN = '6527627892:AAH_brpnVCyzHl7AahqDOa-xkV2LsE4ciDc'
wikipedia.set_lang('uz')


# Configure logging


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher


bot = Bot(token=API_TOKEN)


dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])

async def send_welcome(message: types.Message):

    """


    This handler will be called when user sends `/start` or `/help` command

    """

    await message.reply("Wikipedia botga xush kelib san!")




@dp.message_handler()

async def sendWIKI(message: types.Message):
    try:
        # Fetch the summary from Wikipedia
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f'Bu mavzuga oid ko‘plab maqolalar topildi: {e.options}')
    except wikipedia.exceptions.PageError:
        await message.answer('Bu mavzuga oid maqola topilmadi')
    except Exception as e:
        await message.answer(f'Noma’lum xato yuz berdi: {e}')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)