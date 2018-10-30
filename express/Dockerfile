FROM node:8.9.1

# Update npm cause Error: Cannot find module 'npmlog'
# npm install -g npm@latest && \

RUN useradd --create-home express && \
    mkdir -p /app && chown express:express /app

USER express

WORKDIR /app
COPY package.json /app
COPY package-lock.json /app
RUN npm install

ENV PATH=$PATH:/app/node_modules/.bin