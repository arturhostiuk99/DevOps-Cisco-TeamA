#!/bin/bash

# Check the number of passed arguments
if [ "$#" -ne 2 ]; then
	echo "Використання: $0 <шлях_до_директорії> <розширення_файлів>"
	exit 1
fi

# Get arguments
directory="$1"
extension="$2"

# Check whether the directory exists
if [ ! -d "$directory" ]; then
	echo "Директорія '$directory' не існує."
	exit 1
fi

# Find files with the specified extension and output them
find "$directory" -type f -name "*.$extension" -print

