FROM continuumio/anaconda3
WORKDIR app/
RUN apt-get -y update && apt-get -y install git
RUN git clone https://github.com/woodElec/neumonia_detector.git
RUN conda create -n tf tensorflow # && conda activate tf
RUN cd neumonia_detector && pwd && pip install -r requirements.txt
CMD ["python", "neumonia_detector/detector_neumonia.py"]