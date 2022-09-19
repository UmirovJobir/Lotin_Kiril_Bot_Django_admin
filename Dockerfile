#!/bin/sh

FROM python:3.10.4
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

RUN chmod +x entrypoint.sh
COPY entrypoint.sh /usr/src/app
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]