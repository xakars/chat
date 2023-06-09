# Распознаём речь

В проекте реализованы боты-помощники, которые умеют отвечать на одноптипные вопросы от пользователей.

[telegram_bot](https://t.me/chat_voice_dvmn3423_bot) и [vk_bot](https://vk.com/public219929952)

Пример работы telegram бота:

![video-to-gif](https://user-images.githubusercontent.com/73193926/232184885-6bc611ea-5b05-437c-9b61-9a23ee93f81d.gif)


### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости

```sh
pip install -r requirements.txt
```
В проекте используется Dialogflow. С помощью Dialogflow можно создавать различные типы чат-ботов, которые могут взаимодействовать с пользователями через текстовые сообщения, голосовые команды, картинки и другие форматы. Платформа использует машинное обучение и обработку естественного языка для понимания намерений пользователя и обработки запросов, что позволяет создавать более интеллектуальные и эффективные чат-боты.

Для развертывания проекта необходимо прописать переменные окружения в файле .env, такие как:
```
BOT_TOKEN={токен телеграм бота}
GOOGLE_APPLICATION_CREDENTIALS={путь к файлу учетных данных (credentials) сервисного аккаунта Google Cloud}
PROJECT_ID={идентификатор проекта в Google Cloud}
VK_TOKEN={токен вконтакте бота}
LOGGER_BOT_TOKEN={токен логгер бота в телеграм}
ADMIN_CHAT_ID={id пользовтеля теграм, которому будут оправлятся отчеты логгер бота}
```

После выполните следующие команды: 
```
python3 bot.py
```
```
python3 vk_bot.py
```
Для натренировки бота используйте `create_intent.py` аргументом укажите путь до файла тренировочными фразами
в формате:
```json
{
  "Устройство на работу": {
    "questions": [
      "Как устроиться к вам на работу?",
      "Как устроиться к вам?",
      "Как работать у вас?",
      "Хочу работать у вас",
      "Возможно-ли устроиться к вам?",
      "Можно-ли мне поработать у вас?",
      "Хочу работать редактором у вас"
    ],
    "answer": "Если вы хотите устроиться к нам, напишите на почту game-of-verbs@gmail.com мини-эссе о себе и прикрепите ваше портфолио."
  }
}
```
Например:
```
python3 create_intent.py --path ./path_to_training_phrases
```
По умолчанию скрипт будет искать тренировочные фразы в текущем каталоге в файле `training.json`