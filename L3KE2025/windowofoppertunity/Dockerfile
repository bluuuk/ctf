FROM node:22-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache \
    chromium \
    nss \
    freetype \
    harfbuzz \
    ca-certificates \
    ttf-freefont \
    dumb-init

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm i

RUN adduser -D -u 1001 bot && \
    mkdir -p /home/bot && \
    chown -R bot:bot /home/bot /app

COPY . .

USER bot

ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser
ENV NODE_ENV=production
ENV FLAG="L3AK{temp_flag}"
ENV COOKIE_SECRET="1234"

EXPOSE 3000

ENTRYPOINT ["dumb-init", "--"]

CMD ["node", "index.js"]
