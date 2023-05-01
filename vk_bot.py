import random
import os
import telegram
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from detect_text import detect_intent_texts
import logging
from logger import TelegramLogsHandler


logger = logging.getLogger()

def handle_user_message(project_id, event, vk_api):
    language_code = "ru"
    message = detect_intent_texts(project_id, event.user_id, event.text, language_code)
    if message.intent.is_fallback:
        return
    else:
        message = message.fulfillment_text
    vk_api.messages.send(
        user_id=event.user_id,
        message=message,
        random_id=random.randint(1,1000)
    )

if __name__ == "__main__":
    try:
        load_dotenv()

        logger.setLevel(logging.INFO)
        logger_bot_token = os.environ['LOGGER_BOT_TOKEN']
        logger_bot = telegram.Bot(token=logger_bot_token)
        admin_chat_id = os.environ["ADMIN_CHAT_ID"]
        bot_logger_handler = TelegramLogsHandler(logger_bot, admin_chat_id)
        logger.addHandler(bot_logger_handler)

        project_id = os.environ["PROJECT_ID"]
        vk_token = os.environ["VK_TOKEN"]
        vk_session = vk.VkApi(token=vk_token)
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        logger.info('Vk_bot started')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                handle_user_message(project_id, event, vk_api)
    except Exception as err:
        logger.exception(f"Бот упал с ошибкой:\n, {err}")
