import requests
from django.conf import settings
from django.utils.timezone import localtime
from rest_framework import status
import json

def send_telegram(habit):
    local_habit_time = localtime(habit.time)
    formatted_time = local_habit_time.strftime("%H:%M")

    text = f"{habit.action} запланировано на сегодня на {formatted_time}"
    chat_id = habit.user.tg_chat_id

    # Проверка наличия tg_chat_id
    if chat_id:
        params = {"text": text, "chat_id": chat_id}
        response = requests.post(
            f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage", data=params
        )
        if response.status_code != status.HTTP_200_OK:
            # Получаем JSON-ответ для более точного анализа ошибок
            try:
                error_data = response.json()
                error_message = error_data.get('description', 'Unknown error')
                print(f"Ошибка при отправке сообщения в Telegram: {error_message}")
            except json.JSONDecodeError:
                print(f"Ошибка при отправке сообщения в Telegram: {response.text}")
    else:
        print(f"Telegram chat ID не найден для пользователя {habit.user}")