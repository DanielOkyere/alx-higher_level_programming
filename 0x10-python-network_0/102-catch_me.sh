#!/bin/bash
#Respong "You got me!"
curl -s -X PUT -H 'Origin: HolbertonSchool' -L --max-redirs -1 -d "user_id=98" "0.0.0.0:5000/catch_me"
