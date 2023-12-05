#!/bin/bash
# Get the HTTP METHODS the link allows
curl -f -i -s -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
