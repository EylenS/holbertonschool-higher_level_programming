#!/bin/bash
# takes in a URL, sends a req to, and displays the size in bytes of the body
curl -sI $1 | grep -i 'Content-Length' | awk '{print $2}'
