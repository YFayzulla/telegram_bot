from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6456617315:AAGixsiR4jaG7z3DXLNF8SPge0UEOJ6G1BQ6456617315:AAGixsiR4jaG7z3DXLNF8SPge0UEOJ6G1BQ'
BOT_USERNAME: Final = '@wikipediya_new_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello homeless are you soo free do your tasks or homework,baby')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('what do you wont')


async def costum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Fuck you')

    # Responses


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in text:
        return 'hey there!'

    if 'how ore you' in text:
        return 'I am good!'

    if 'i love you' in text:
        return 'fuck you!'
    return 'I dont understand what you wrote .!. '


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User({update.message.chat.id}) in {message_type}:"{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Start bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', start_command))
    app.add_handler(CommandHandler('custom', start_command))
    # app.add_handler(CommandHandler('start',start_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERROR
    app.add_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)




