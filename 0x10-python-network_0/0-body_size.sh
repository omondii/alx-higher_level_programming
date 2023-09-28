#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL
curl -sI "$1" | grep "content-length" | cut -d ' ' -f 2
