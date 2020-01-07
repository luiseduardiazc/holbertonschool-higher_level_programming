#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
curl -sd -d "email=hr%40holbertonschool%2Ecom&subject=I+will+always+be+here+for+PLD" -X POST "$1"
