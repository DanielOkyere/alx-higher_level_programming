#/bin/bash
# Makes a request and print the size of the request
curl -s "$1" | wc -c
