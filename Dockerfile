# Dockerfile
# docker build . -t fastapi-web
# docker run -d -p 8000:8000 fastapi-web

# pull the official docker image
FROM python:3.10.9-buster
# FROM python:3.9.4-slim

# set work directory
WORKDIR /app
#WORKDIR $WORKDIR
ENV PYTHONPATH "${PYTHONPATH}:/"
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHON_VERSION 3.10.9
ENV PYTHONPATH "${WORKDIR}:${PYTHONPATH}"

RUN pip3 install -U pip

# install dependencies
COPY requirements.txt .

RUN pip3 install -r requirements.txt

# copy project
COPY ./src .

EXPOSE 8000

# Execute
CMD ["python", "main.py"]
