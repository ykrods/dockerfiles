FROM node:8.9.1

# Update npm cause Error: Cannot find module 'npmlog'
# npm install -g npm@latest && \

RUN useradd --create-home express

RUN mkdir /code && chown express:express /code

USER express

WORKDIR /code

ADD package.json /code
ADD package-lock.json /code

RUN npm install

ENV PATH=/code/node_modules/.bin:$PATH
