FROM python:3.13-alpine

RUN pip install flask

COPY flag.txt /flag.txt

WORKDIR /app

COPY app.py .

CMD ["python3", "/app/app.py"]
