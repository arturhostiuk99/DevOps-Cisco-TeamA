#!/bin/bash

# Check if the required arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory path> <file extension>"
    exit 1
fi

# Get the arguments from the command line
directory="$1"
extension="$2"

# Check if the directory exists
if [ ! -d "$directory" ]; then
    echo "Directory '$directory' does not exist."
    exit 1
fi

# Use the find command to search for files with the specified extension
file_count=$(find "$directory" -type f -name "*.$extension" | wc -l)

# Display the result
echo "Number of files with extension '$extension' in directory '$directory': $file_count"
