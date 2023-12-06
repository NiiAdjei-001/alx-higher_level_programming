#!/bin/bash
# Send a POST HTTP Request to a link. param: { email = ...; subject = ...}
curl -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' -f -s "$1"