FROM python:3.7-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

ENV GUNICORN_CMD_ARGS="--bind=0:8000 --chdir=./app/app"

CMD [ "gunicorn", "wsgi:application" ]