FROM ubuntu:18.04

ADD . /app
WORKDIR /app
ENV PATH="/opt/py3/bin:${PATH}"

RUN apt-get update \
    && apt-get -y install --no-install-recommends gcc python3-dev python3 virtualenv \
    && virtualenv --python python3 /opt/py3 \
    && pip install -r requirements.txt -r test-requirements.txt \
    && apt -y autoremove gcc python3-dev \
    && apt-get clean all
