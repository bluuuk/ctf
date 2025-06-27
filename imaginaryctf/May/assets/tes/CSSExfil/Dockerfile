FROM node:alpine
RUN mkdir -p /home/node/app/node_modules && chown -R node:node /home/node/app
WORKDIR /home/node/app
COPY blind-css-exfiltration/node_modules /home/node/app/node_modules 
COPY blind-css-exfiltration/css-exfiltrator-server.js ./
COPY blind-css-exfiltration/package*.json ./
CMD ["node", "css-exfiltrator-server.js"]