FROM python:3.9.0

WORKDIR /app


COPY /docker/requirements.txt /app/
COPY /src/ /app/
COPY /test/ /app
COPY /data /app

WORKDIR /app
RUN pip3 install -r requirements.txt

CMD [ "python3", "-m", "app"]
