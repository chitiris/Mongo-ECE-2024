#! /usr/bin/bash
#https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/
docker pull mongodb/mongodb-community-server:latest
docker run --name mongodb -p 27017:27017 -d mongodb/mongodb-community-server:latest
docker ps