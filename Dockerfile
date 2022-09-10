FROM python:3.10

RUN mkdir -p /usr/src/app
ADD .    /usr/app
WORKDIR /usr/app/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# CMD [ "python","main.py" ]