#!/bin/sh

# FROM python:3.10.4
# WORKDIR /usr/src/app

# RUN pip install --upgrade pip
# COPY requirements.txt /usr/src/app
# RUN pip install -r requirements.txt

# RUN python manage.py makemigrations
# RUN python manage.py migrate

# RUN chmod +x entrypoint.sh
# COPY entrypoint.sh /usr/src/app
# ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY requirements.txt ./code
COPY . .


RUN apt-get update \
    && apt-get install -yyq netcat

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

COPY entrypoint.sh ./code
ENTRYPOINT [ "sh", "./code/entrypoint.sh" ]