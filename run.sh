#!/bin/bash

cd "$(dirname "$0")"

docker run --name my-next-game --mount type=bind,source="${pwd}/app",target=/app -p 5000:5000 --link redis-stack-server:db  my-next-game:latest