#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory path> <file extension>"
    exit 1
fi

directory="$1"
extension="$2"

if [ ! -d "$directory" ]; then
    echo "Directory '$directory' does not exist."
    exit 1
fi

file_count=$(find "$directory" -type f -name "*.$extension" | wc -l)

echo "Number of files with extension '$extension' in directory '$directory': $file_count"
