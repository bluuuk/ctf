FROM oven/bun:1

WORKDIR /app

COPY package.json bun.lock ./
RUN bun install

RUN bunx playwright@1.51.1 install
RUN /usr/local/bin/playwright install-deps chromium
COPY . .

EXPOSE 3000

ENV FLAG=flagge{standard_docker_flagge}
ENV DEBUG=pw:api,pw:browser*

CMD ["bun", "run", "src/index.ts"]
