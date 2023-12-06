#!/bin/bash
# Send a POST HTTP Request to a link. param: { email = ...; subject = ...}
curl -F 'email=test@gmail.com;type=text/email' -F 'subject=I will always be here for PLD;type=text/plain' -f -s "$1"
