# Google Cloud Functions supports v8.11.1 as of 2018-12-02
FROM node:8.11.1

# Update npm
RUN npm install -g npm@latest && \
  useradd --create-home firebase

USER firebase

# How to prevent permission error
# https://docs.npmjs.com/getting-started/fixing-npm-permissions#option-two-change-npms-default-directory
RUN mkdir /home/firebase/.npm-global && \
    npm config set prefix '~/.npm-global' && \
    npm install -g firebase-tools

ENV PATH /home/firebase/.npm-global/bin:$PATH

ENTRYPOINT ["firebase"]
CMD ["serve", "--host", "0.0.0.0"]
