# syntax=docker/dockerfile:1

FROM python:3.10

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

# To publish the port 8000, docker run -p 8000:8000
EXPOSE 8000

CMD ["python", "manage.py", "runserver"]