FROM ubuntu:20.04

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y wget mc tmux nano build-essential rsync libgl1 python3-pip


RUN pip install tf-explain
RUN pip install tensorflow==2.6.0
RUN pip install keras==2.6.0
RUN pip install opencv-python
RUN pip install Pillow
RUN pip install protobuf==3.20.1

COPY test.py /test.py
COPY images /images

CMD python3 test.py
