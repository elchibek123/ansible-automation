#!/bin/bash

package=$(dpkg -l | grep -i "$1")
if [ -z "$package" ]; then
    echo "No package found"
    exit 1
else
    echo "Found package: $package"
    exit 0
fi