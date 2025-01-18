#!/bin/bash

container=$(docker ps | grep -i "$1")
if [ -z "$container" ]; then
    echo "No container found"
    exit 1
else
    echo "Found container: $container"
    exit 0
fi