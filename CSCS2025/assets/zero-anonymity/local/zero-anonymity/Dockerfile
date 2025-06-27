FROM node:latest

ADD server /home/node/app
RUN mkdir /home/node/app/node_modules
RUN chown -R node:node /home/node/app

WORKDIR /home/node/app
USER node
RUN npm install
EXPOSE 9000

CMD [ "node", "server.js" ]
