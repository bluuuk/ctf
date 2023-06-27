FROM debian:buster-slim

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update --fix-missing && \
    apt-get install -y --no-install-recommends socat python3-minimal && apt-get clean

WORKDIR /root
ADD vm vm
ADD run.py run.py

RUN chmod +x vm

ENTRYPOINT [ "socat", "tcp-l:1024,reuseaddr,fork", "EXEC:'python3 run.py'" ]
