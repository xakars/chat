import random
import os

import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from detect_text import detect_intent_texts


def echo(event, vk_api):
    response = detect_intent_texts(project_id, event.user_id, event.text, "ru")

    vk_api.messages.send(
        user_id=event.user_id,
        message=response,
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
            echo(event, vk_api)