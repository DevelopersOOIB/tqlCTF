FROM ubuntu

RUN mkdir /app
RUN apt update -y && apt install python3 -y && apt install python3-pip -y
RUN python3 -m pip install flask

WORKDIR /app
COPY ./main.py /app/app.py
COPY ./templates /app/templates
COPY ./static /app/static
COPY ./authbypass.db /app/authbypass.db

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
