#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays size of the body in bytes
curl -s "$1" | wc -c
