#!/bin/bash
# displays http body size
curl -s -i "$1" | grep "Content-Length"
