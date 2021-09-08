FROM python:3.9.7-buster

RUN pip install pytest==6.2.5 pytest-cov==2.12.1

RUN mkdir -p /work

WORKDIR /work

COPY ./test_test.py /work/