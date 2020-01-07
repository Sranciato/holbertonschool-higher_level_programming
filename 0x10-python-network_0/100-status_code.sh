#!/bin/bash
# get status code of url
curl -LI $2 -o /dev/null -w '%{http_code}' -s
