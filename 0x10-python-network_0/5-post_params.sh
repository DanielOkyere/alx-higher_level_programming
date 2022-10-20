#!/bin/bash
# post params using curl
curl -sL -X POST -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
