# Chat_bot

В проекте реализованы боты-помощники, которые умеют отвечать на одноптипные вопросы от пользователей.

[telegram_bot](https://t.me/chat_voice_dvmn3423_bot) и [vk_bot](https://vk.com/public219929952)


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

