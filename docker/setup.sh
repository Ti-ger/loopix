#!/bin/bash
docker rmi loopix_server:latest
docker build -t loopix_server:latest server/
docker-compose up
