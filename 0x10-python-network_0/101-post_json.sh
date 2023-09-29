#!/bin/bash
# Send a JSON request
curl -sXH POST "Content-Type: application" -d @"$2" "$1"
