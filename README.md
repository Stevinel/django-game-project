# Задание
![image](https://user-images.githubusercontent.com/72396348/137326383-b395fc8e-d8f2-4de0-9721-5e607729377a.png)

# Установка
- Склонировать репозиторий https://github.com/Stevinel/test_outofcloud
- Установить виртуальное окружение python -m venv venv
- Установить зависимости pip install -r requiremets.txt
- Создать и сделать миграции python manage.py makemigrations & python manage.py migrate
- Создать суперпользователя python manage.py createsuperuser
- Запустить сервер python manage.py runserver
- Зайти в Postman для тестирования.
- Отправить POST запрос по эндпойнту http://127.0.0.1:8000/api/v1/emails/ с ключом email
- Можно смотреть созданные данные в админке http://127.0.0.1:8000/admin/
