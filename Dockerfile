FROM python:3.9

RUN apt-get update && \
    apt-get install -y python3-opencv poppler-utils

RUN mkdir /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python3", "/app/manage.py", "runserver", "0.0.0.0:8000"]