
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt main.py urls.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "main.py"]