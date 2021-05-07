FROM jupyter/base-notebook:lab-2.2.5

USER root
# python3 setup
RUN apt-get update && apt-get install -y graphviz git


WORKDIR /usr/src/app

COPY . $WORKDIR

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir "dask[distributed]"