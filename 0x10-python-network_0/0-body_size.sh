#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays
# the size of the body of the responseclear
curl -sI "$1" | grep "content-length" | cut -d ' ' -f 2
