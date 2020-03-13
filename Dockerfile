FROM python:3.7

COPY ./requirements.txt requirements.txt
COPY ./setup.py setup.py
COPY ./entry.py entry.py
COPY ./app /app

RUN python setup.py develop

EXPOSE 8080