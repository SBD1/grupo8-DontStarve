FROM python:3.10

RUN mkdir -p /usr/src/app
ADD .    /usr/app
WORKDIR /usr/app/src
COPY requirements.txt ./
RUN pip install -r requirements.txt
