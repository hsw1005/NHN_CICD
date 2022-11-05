FROM gradle:jdk8

COPY ./build ./
RUN pwd
RUN ls -alh
