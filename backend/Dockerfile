FROM python:3.11.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /api
WORKDIR /api

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

