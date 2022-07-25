#!/bin/bash

# docker run --rm -d testserver --name "testserver-api-gateway"
docker run --rm -p 5000:5000  --name "testserver-api-gateway" testserver
