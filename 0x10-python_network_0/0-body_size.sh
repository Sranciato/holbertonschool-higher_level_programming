#!/bin/bash
# displays the size of the body
curl -sI "$@" | grep Content-Length | cut -d" " -f2
