#!/bin/bash
# Send http  DELETE response body; Handles redirects -L; Handle fail status -f
curl -s -f -L -X DELETE "$1"
