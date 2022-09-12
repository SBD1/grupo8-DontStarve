FROM python:3.10

RUN mkdir -p /usr/src/app
ADD /src    /usr/app
WORKDIR /usr/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
