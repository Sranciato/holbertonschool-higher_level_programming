#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI "$@" | grep Allow | cut -d" " -f2-
