#!/bin/bash
# displays http body size
curl -s -I "$1" | grep "Content-Length" | cut -d " " -f 2
