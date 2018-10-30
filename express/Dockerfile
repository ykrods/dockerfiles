FROM node:8.9.1

# Update npm cause Error: Cannot find module 'npmlog'
# npm install -g npm@latest && \

RUN useradd --create-home express

USER express

RUN mkdir /home/express/.npm-global && \
    npm config set prefix '~/.npm-global' && \
    npm install -g express nodemon

ENV PATH=/home/express/.npm-global/bin:$PATH
ENV NODE_PATH=/home/express/.npm-global/lib/node_modules
