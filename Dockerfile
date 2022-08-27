FROM python:latest

RUN apt-get update -y && \
    apt-get install python3-opencv -y 

RUN pip install opencv-contrib-python-headless

WORKDIR /home/src

COPY . ./
RUN pip install -r requirements.txt
