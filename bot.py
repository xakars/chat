from dotenv import load_dotenv
import os
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from detect_text import detect_intent_texts

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте!")


def chat(update: Update, context: CallbackContext):
    project_id = os.environ["PROJECT_ID"]
    chat_id = update.effective_chat.id
    text = update.message.text
    language_code = "ru"
    response = detect_intent_texts(project_id, chat_id, text, language_code)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def main():
    load_dotenv()
    token = os.environ["BOT_TOKEN"]
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), chat)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
