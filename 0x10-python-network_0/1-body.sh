#!/bin/bash
# Display body of the response from curl
curl -X GET "$1" | wc -c
