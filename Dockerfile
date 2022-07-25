FROM ubuntu:latest

COPY install.sh /tmp

RUN apt update; apt install -y python3 python3-venv; mkdir /app 

COPY service.sh /app
COPY install.sh /tmp
RUN bash /tmp/install.sh
COPY test-service.py /app/app.py


ENTRYPOINT ["/app/service.sh"]