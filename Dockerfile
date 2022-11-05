FROM gradle:jdk8

COPY ./build ./
RUN pwd

ENTRYPOINT ['ls', '-alh']
