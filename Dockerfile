FROM continuumio/miniconda3
MAINTAINER Jorman Copete
WORKDIR /
COPY *.py ./
COPY *.txt ./
RUN conda create -n tf tensorflow
RUN pip install -r requirements.txt
