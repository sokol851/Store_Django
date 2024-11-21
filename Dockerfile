FROM python:3.11

WORKDIR /storeDjango

COPY requirements.txt .

COPY .env .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Команда для запуска приложения при старте контейнера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]