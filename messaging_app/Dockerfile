# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /messaging_app

COPY requirements.txt /messaging_app/requirements.txt

RUN pip install -r requirements.txt

COPY . /messaging_app

EXPOSE 8000

CMD ["python", "manage.py", "runserver"]