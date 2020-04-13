FROM ubuntu:16.04
USER root
# install required binaries
RUN apt-get update \
    && apt-get install -y python3 \
    && apt-get install -y python3-pip \
    && apt-get install screen -y \
    && apt-get install htop -y \
    && apt-get install openssh-client -y \
    && apt-get install vim -y

# install pip requirements
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

# copy project to docker image
# COPY WorkSpace S20-team7-project/WorkSpace
# RUN cd S20-team7-project/WorkSpace
# RUN pip3 install --upgrade pip
# RUN pip3 install -r requirements.txt
