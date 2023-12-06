#!/bin/bash
# Send http  DELETE response body; Handles redirects -L; Handle fail status -f
curl -s -L -X DELETE "$1"
