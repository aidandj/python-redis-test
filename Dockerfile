FROM python:3.7-alpine

WORKDIR /code
RUN pip install pipenv
COPY . .
RUN pipenv install --deploy --system