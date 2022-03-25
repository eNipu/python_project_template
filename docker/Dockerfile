FROM python:3.9.0 as base
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /

# RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev python3-pip
RUN pip3 install --upgrade pip
# RUN pip3 install --upgrade setuptools
# RUN pip3 install --upgrade wheel
# RUN pip3 install --upgrade twine

WORKDIR /app


COPY /docker/requirements.txt /app/
COPY /src/ /app/
COPY /test/ /app
COPY /data /app

WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["python3", "src/app.py"]
