FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию для проекта
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё приложение
COPY . .

# Меняем рабочую директорию — теперь manage.py будет найден
WORKDIR /app/src

RUN chmod +x /app/local_entrypoint.sh

CMD ["bash", "/app/local_entrypoint.sh"]
