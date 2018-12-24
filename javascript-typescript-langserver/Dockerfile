FROM node:8.9.1

# Update npm cause Error: Cannot find module 'npmlog'
# npm install -g npm@latest && \

RUN useradd --create-home langserver

USER langserver

RUN mkdir /home/langserver/.npm-global && \
    npm config set prefix '~/.npm-global' && \
    npm install -g javascript-typescript-langserver

ENV PATH=/home/langserver/.npm-global/bin:$PATH
ENV NODE_PATH=/home/langserver/.npm-global/lib/node_modules
