FROM alpine:latest

ENV VEGADNS_CLI master

ADD . /opt/vegadns-cli

RUN apk --update add python3 py3-setuptools curl bash py3-pip

RUN pip3 install -r /opt/vegadns-cli/requirements.txt

WORKDIR /opt/vegadns-cli

# Init stuff
RUN curl -L -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.1.3/dumb-init_1.1.3_amd64 && \
    chmod +x /usr/local/bin/dumb-init

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

ENV PYTHONUNBUFFERED 1
