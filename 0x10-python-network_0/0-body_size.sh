#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the response
# s silent option, quiet mode, so don't show more than what i am asking for
# wc -c count the number of bytes
curl -s "$1" | wc -c
