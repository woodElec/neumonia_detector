FROM python:3.9
RUN apt-get update && apt-get install -y

RUN pip install -U pip
RUN pip install python-xlib
COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY . /app
WORKDIR /app
CMD ["python", "detector_neumonia.py"]