# https://fossil-scm.org/fossil/doc/trunk/www/index.wiki

FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y curl

RUN useradd --create-home fossil

USER fossil
WORKDIR /home/fossil/
RUN mkdir /home/fossil/.bin && \
  curl -s -O https://fossil-scm.org/home/uv/fossil-linux-x64-2.14.tar.gz && \
  tar xzvf fossil-linux-x64-2.14.tar.gz --directory /home/fossil/.bin && \
  mkdir /home/fossil/projects

ENV PATH /home/fossil/.bin:$PATH
CMD ["fossil"]