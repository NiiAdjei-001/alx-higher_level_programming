#!/bin/bash
# displays http GET response body; Handles redirects -L; Handle fail status -f
curl -s -f -L "$1"
