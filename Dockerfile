FROM python

WORKDIR /app

RUN apt-get update -y

RUN apt-get install tk -y

COPY *.txt ./

ADD . /app

RUN conda create -n tf tensorflow # && conda activate t

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt

#CMD ["python", "neumonia_detector/detector_neumonia.py"]
