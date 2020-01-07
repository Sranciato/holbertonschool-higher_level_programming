#!/bin/bash
# get status code of url
curl -LI "$@" -o /dev/null -w '%{http_code}' -s
