FROM ghcr.io/puppeteer/puppeteer:24.2.1

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install

COPY . .

ENV DOMAIN="challenge-domain.com"
ENV FLAG="FLAG{NOT_THE_REAL_FLAG}"

CMD ["yarn", "start"]
