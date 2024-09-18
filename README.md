В данном проекте реализована бэкенд-часть веб-приложения.

Приложение для приобретения полезных привычек и избавление от оных. 

Сервис интегрирован с телеграмом.

Пользователь регистрируется, добавляет свою привычку и время для ее выполнения. При регистрации, необходимо указать ID телеграмма.

Работа с приложением:
Клонируем приложение из github-a
Активируем виртуально окружение
Устанавливаем зависимости pip install -r requirements.txt либо если у вас poetry то poetry install
Создаем и вносим данные в файл .env, все что указаны в .env.sample
Создаем зависимости и применяем их
Установите Redis, запустите командой redis-server
Запускаем django приложение командой python3 manage.py runserver. Если у вас poetry то используем команду python manage.py runserver
В терминале запустите celery worker командой: celery -A config worker -l INFO # для Mac и Linux celery -A config worker -l INFO -P eventlet # для Windows
В другом терминале запустите celery beat командой: celery -A config beat -l info -S django


Запуск приложения через docker

В терминале введите команду docker-compose up -d --build