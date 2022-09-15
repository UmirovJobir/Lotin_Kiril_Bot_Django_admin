FROM python:3.10

# ENV PYTHONUNBUFFERED=1

WORKDIR /app
# COPY requirements.txt ./app
COPY . . 

RUN apt-get update \
    && apt-get install -yyq netcat

RUN chmod +x entrypoint.sh
RUN pip install -r requirements.txt


EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT ["sh", "./entrypoint.sh"]