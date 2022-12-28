# Dockerfile

# pull the official docker image
FROM python:3.10.9-buster
# FROM python:3.9.4-slim

# set work directory
WORKDIR /app
RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHON_VERSION 3.10.9
ENV PYTHONPATH=$WORKDIR:$PYTHONPATH

RUN pip3 install -U pip

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .