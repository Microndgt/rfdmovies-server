FROM ubuntu
MAINTAINER Kevin <dgt_x@foxmail.com>
LABEL description="rfdmovies base on flask" version="0.1"

RUN mv /bin/sh /bin/sh.bak && ln -snf /bin/bash /bin/sh

USER root

COPY /utils/sources.list /etc/apt/sources.list

RUN apt-get update --fix-missing --yes && DEBIAN_FRONTEND=noninteractive apt-get -f install apt-utils --no-install-recommends --yes
RUN apt-get -y install apt-transport-https ca-certificates curl software-properties-common wget

RUN apt-get install gcc vim zip git --yes

RUN apt-get install libdbd-mysql-perl mysql-client python3 python3-pip --yes
RUN apt-get clean &&  apt-get autoclean
RUN ln -s $(which python3) /usr/bin/python &&  ln -s $(which pip3) /usr/bin/pip
RUN pip install --upgrade pip virtualenv ipython

RUN mkdir -p /opt/rfdmovies
COPY . /opt/rfdmovies/
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN -H pip install -r /opt/rfdmovies/requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /opt/rfdmovies
CMD ["sh", "run.sh"]
