FROM python:3.13-alpine

RUN pip install flask

COPY flag.txt /flag.txt

RUN mv /flag.txt "/flag_$(cat /dev/urandom | head -c 45 | hexdump | tr -d ' \n').txt"

WORKDIR /app

COPY app.py .

USER 1001

CMD ["python3", "/app/app.py"]
