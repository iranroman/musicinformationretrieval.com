FROM python:3.12-bookworm as base

RUN apt-get update && \
    apt-get dist-upgrade -y && \

RUN pip install --upgrade pip

RUN mkdir -p /code
WORKDIR /code
ADD requirements.txt Makefile .
RUN make venv/
ADD * .

FROM base as test
RUN make test

FROM base as run
RUN make



