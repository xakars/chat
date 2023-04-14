from dotenv import load_dotenv
import telegram
import os
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from detect_text import detect_intent_texts
import logging
from logger import TelegramLogsHandler


logger = logging.getLogger()

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте!")


def chat(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    text = update.message.text
    language_code = "ru"
    message = detect_intent_texts(project_id, chat_id, text, language_code).fulfillment_text
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


if __name__ == '__main__':
    load_dotenv()

    logger.setLevel(logging.INFO)
    logger_bot_token = os.environ['LOGGER_BOT_TOKEN']
    logger_bot = telegram.Bot(token=logger_bot_token)
    admin_chat_id = os.environ["ADMIN_CHAT_ID"]
    bot_logger_handler = TelegramLogsHandler(logger_bot, admin_chat_id)
    logger.addHandler(bot_logger_handler)

    token = os.environ["BOT_TOKEN"]
    project_id = os.environ["PROJECT_ID"]
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), chat)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    while True:
        try:
            updater.start_polling()
        except Exception as err:
            logger.exception(f"Бот упал с ошибкой:\n, {err}")
