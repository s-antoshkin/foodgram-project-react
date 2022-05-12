FROM python:3.7-slim

RUN pip install --upgrade pip

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir

CMD [ "gunicorn", "app.wsgi:application", "--bind", "0:8000" ]