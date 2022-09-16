FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get update \
    && apt-get install -yyq netcat
RUN pip install -r requirements.txt
COPY . /code/

EXPOSE 8000

COPY entrypoint.sh .
ENTRYPOINT ["sh", "entrypoint.sh"]