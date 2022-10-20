#!/bin/bash
# List all HTTP Method that a server will accept
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
