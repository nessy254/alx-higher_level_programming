#!/bin/bash
# A script that measures the size of the body of a response
curl -s "$1" | wc -c
