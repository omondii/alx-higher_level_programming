#!/bin/bash
#A bash script that takes in a URL and displays all HTTP methods
curl -siX OPTIONS $1 | grep "Allow" | cut -d " " -f2-
