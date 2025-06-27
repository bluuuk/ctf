# zero-anonymity

## Pre-requisites

- [Circom](https://docs.circom.io/)
- [Snarkjs](https://www.npmjs.com/package/snarkjs) (and `node`)
- [docker-compose](https://docs.docker.com/)

## Run

Run the following in `local/zero-anonymity`:
```bash
$ bash build.sh
```

Add your public hash from `public.json` to the list `users` in `server/server.js` if you want to be able to authenticate.

Then build and start the docker container with the server in `local/`:
```bash
$ docker compose up --build
```