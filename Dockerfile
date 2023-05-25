FROM python:3.10

RUN apt-get update -qq && \
    apt-get install -y -qq rabbitmq-server && \
    apt-get clean all && \
    rm -rf /var/apt/lists/* && \
    rm -rf /var/cache/apt/*

ENV PYTHONUNBUFFERED=1 \
    HOME=/app

WORKDIR ${HOME}
EXPOSE 81 444 8002

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY . /app