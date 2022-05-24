#!/bin/sh

docker run -dp 8000:8000 --name=tabula-server --network=net tabula-server
