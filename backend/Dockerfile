FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Instala las dependencias del sistema necesarias para mysqlclient
RUN apt-get update && apt-get install -y \
    python3-dev \
    default-libmysqlclient-dev \
    build-essential

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
