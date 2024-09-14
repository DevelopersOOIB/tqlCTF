# we need python, pip, flask, yara, also waitress
FROM ubuntu:latest
RUN mkdir -p /usr/src/app
RUN apt update
RUN /bin/bash -c 'apt install -y python3 python3-pip yara'
RUN /bin/bash -c 'python3 -m pip install flask waitress'
WORKDIR /usr/src/app
EXPOSE 80
CMD python3 waitress_server.py