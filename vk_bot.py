import random
import os

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from detect_text import detect_intent_texts


def chat(event, vk_api):
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
    load_dotenv()
    project_id = os.environ["PROJECT_ID"]
    vk_token = os.environ["VK_TOKEN"]
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            chat(event, vk_api)
