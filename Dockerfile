
# base image
FROM python:3.10.1-slim-buster

# working dir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


# add/install requirements and copy app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# run 
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh