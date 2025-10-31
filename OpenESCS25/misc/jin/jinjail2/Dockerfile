FROM alpine

RUN apk add py3-flask

COPY flag.txt /flag.txt

RUN mv /flag.txt "/$(cat /dev/urandom | head -c 45 | hexdump | tr -d ' \n')_flag.txt"

WORKDIR /app

COPY app.py .

USER 1001

CMD ["python3", "/app/app.py"]
