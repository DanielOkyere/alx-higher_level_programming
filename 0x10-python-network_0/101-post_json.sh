#!/bin/bash
#Sends JSON POST request
curl -sH "Content-Type: application/json" -d @"$2" "$1"
