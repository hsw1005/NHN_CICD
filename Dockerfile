FROM gradle:jdk8

COPY ./build ./
RUN ls -alh
