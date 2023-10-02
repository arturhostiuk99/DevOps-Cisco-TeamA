#!/bin/bash

# Check the number of passed arguments
 if [ "$#" -ne 2 ]; then
    echo "Використання: $0 <шлях_до_директорії> <текст_для_пошуку>"
    exit 1
fi

# Get arguments
directory="$1"
search_text="$2"

# Check whether the directory exists
if [ ! -d "$directory" ]; then
    echo "Директорія '$directory' не існує."
    exit 1
fi

# Find files that contain the specified text
found_files=$(grep -rl "$search_text")

if [ -z "$found_files" ]; then
    echo "Файли, що містять текст '$search_text', не знайдено у директорії '$directory'."
else
    echo "Файли, що містять текст '$search_text' у директорії '$directory':"
    echo "$found_files"
fi

