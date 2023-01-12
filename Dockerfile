# Dockerfile
# docker build . -t fastapi-web
# docker run -d -p 8000:8000 fastapi-web

# pull the official docker image
FROM python:3.10.9-buster
# FROM python:3.9.4-slim

# set work directory
WORKDIR /app
#WORKDIR $WORKDIR
#ENV PYTHONPATH "${PYTHONPATH}:/app"
# set env variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#ENV PYTHON_VERSION 3.10.9
#ENV PYTHONPATH "${WORKDIR}:${PYTHONPATH}"

#ENV PYTHONPATH="${PYTHONPATH}:/"
ENV PYTHONPATH="${PYTHONPATH}:/app"
ENV SERVER_HOST="0.0.0.0"
ENV PORT=8000

RUN pip3 install -U pip

# install dependencies
COPY requirements.txt .

RUN pip3 install --no-cache-dir --upgrade  -r requirements.txt

# copy project
COPY . .

EXPOSE 8000

# Execute
#CMD ["python", "main.py"]
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]