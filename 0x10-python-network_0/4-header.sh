#!/bin/bash
# script that takes in a URL and displays all HTTP methods the server will accept.
curl -s -H "X-HolbertonSchool-User-Id: 98" -X GET "$1"
