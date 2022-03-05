
# base image
FROM python:3.10.1-slim-buster

# working dir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# env vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add/install requirements and copy app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# run 
CMD python manage.py run -h 0.0.0.0