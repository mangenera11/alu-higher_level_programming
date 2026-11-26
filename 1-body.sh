#!/bin/bash
curl -s -L -w "%{http_code}" "$1" -o /tmp/body

if [ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" = "200" ]; then
    cat /tmp/body
fi
