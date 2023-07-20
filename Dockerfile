FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.9.5
RUN pip install dgl==0.4.3
RUN pip install dgllife==0.2.3
RUN pip install torch==1.9.0

WORKDIR /repo
COPY ./repo
