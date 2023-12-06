#!/bin/bash
# Send a GET HTTP METHODS to a link. Include X-School-User-Id = 89 in req header
curl -f -s --header "X-School-User-Id: 98" "$1"
