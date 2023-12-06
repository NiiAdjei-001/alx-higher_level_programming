#!/bin/bash
# Display only status code of http response:wq
curl -s -o /dev/null -w "%{http_code}" "$1"
