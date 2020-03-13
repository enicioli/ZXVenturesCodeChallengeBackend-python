FROM ubuntu:latest

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip build-essential

WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt

RUN mkdir -p data
RUN mkdir -p log

ENV FLASK_APP=./run.py

EXPOSE 5000
CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]