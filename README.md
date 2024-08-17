## Интернет магазин созданный с помощью Django + Bootstrap

    Запуск сервера с помощью команды: 'python manage.py runserver'
    
    Главная страница: http://localhost:8000
    Админ панель: localhost:8000/admin
    Создать суперпользователя: "python manage.py csu"
        - логин: admin@pow.ru
        - пароль: 12345
    Заполнение базы из бекапа: python manage.py refill
    Заполнение групп пользователей: python manage.py fill_groups

___
## Внимание!! 
Необходимо заполнить данные для SMTP сервера и доступа к базе данных!
####
    Для этого:

    1) Заменить название файла '.env_empty' на '.env' в корне проекта.
    2) В файле заменить необходимые значения.