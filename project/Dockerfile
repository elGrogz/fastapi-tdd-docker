# pull official python base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/src/app

# set env variables
# prevents python writing pyc files to disc (python -B)
ENV PYTHONDONTWRITEBYTECODE 1 
# prevents python buffering to stdout and stderr (python -u)
ENV PTHONUNBUFFERED 1

RUN ls -a

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .