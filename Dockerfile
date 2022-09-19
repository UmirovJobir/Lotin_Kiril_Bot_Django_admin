# FROM python:3.10

# # ENV PYTHONUNBUFFERED=1

# WORKDIR /app
# # COPY requirements.txt ./app
# COPY . . 

# RUN apt-get update \
#     && apt-get install -yyq netcat

# RUN chmod +x entrypoint.sh
# RUN pip install -r requirements.txt


# EXPOSE 8000

# COPY entrypoint.sh ./app 
# ENTRYPOINT ["sh", ".app/entrypoint.sh"]

# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# RUN apt-get update \
#     && apt-get install -yyq netcat

# RUN chmod +x entrypoint.sh
# COPY . /code/

# EXPOSE 8000

# COPY entrypoint.sh .
# ENTRYPOINT ["sh", "entrypoint.sh"]


FROM python:3.10.4
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate