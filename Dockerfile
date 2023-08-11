FROM python:3.12-rc-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt update && apt install -y \
    build-essential libssl-dev xvfb curl wget \
    libffi-dev libpq-dev gcc unzip nano \
    daemonize dbus-user-session fontconfig gettext \
    binutils libproj-dev git && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
