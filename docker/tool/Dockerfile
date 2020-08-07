FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
ADD constraints.txt /code/
RUN pip install -r requirements.txt -c constraints.txt


RUN apt-get update && apt-get install -y \
  vim \
  sudo \
  mecab \
  libmecab-dev \
  mecab-ipadic-utf8

ENV PYTHONPATH "${PYTHONPATH}:/code/getitword"

ADD . /code