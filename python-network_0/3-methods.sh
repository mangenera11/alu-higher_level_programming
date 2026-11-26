#!/bin/bash
# Display all HTTP methods accepted by the server
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d " " -f2-
