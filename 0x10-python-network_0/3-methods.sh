#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" -X DELETE | awk '/Allow/ { print $0 }' | cut -c 8-
