#/usr/bin/bash
# Makes a request and print the size of the request

curl -I $1 | grep "content-length"
