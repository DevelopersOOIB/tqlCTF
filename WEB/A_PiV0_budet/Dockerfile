FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

COPY ./app.py ./app.py
COPY ./drinks.json ./drinks.json
COPY ./templates ./templates
COPY ./static ./static

ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
