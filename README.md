
![image](https://user-images.githubusercontent.com/72396348/182043119-1940ef03-0b27-4a30-9629-d9a8fbe70556.png)

# Установка
- Склонировать репозиторий https://github.com/Stevinel/test_outofcloud
- Установить виртуальное окружение python -m venv venv
- Создать .env файл и добавить переменные со своими данными:
   ```
   DB_ENGINE=
   DB_NAME=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   DB_HOST=
   DB_PORT=
   SECRET_KEY=django-insecure-h&law^nuq%!1()y!v&px+m+cj)sr18s_m4h%efg02o$tni=oq@
   
   !!! В рабочем проекте никогда не указываются данные переменных .env файла !!!
   ```
- Выполнить команды:
   ```
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate --noinput
   docker-compose exec web python manage.py createsuperuser
   docker-compose exec web python manage.py collectstatic --no-input
   ```
- Зайти в Postman для тестирования
- Отправить POST запрос по эндпойнту http://127.0.0.1/api/v1/emails/ с ключом email
- Можно смотреть созданные данные в админке http://127.0.0.1/admin/ 

# Стек
- Python
- Django
- Docker
- Nginx
- Gunicorn
- Postgresql
