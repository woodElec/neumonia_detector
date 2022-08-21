FROM python:latest
RUN apt-get update -y 
RUN apt-get install python3-opencv -y 

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r ./requirements.txt
COPY . /app

CMD ["python", "detector_neumonia.py"]