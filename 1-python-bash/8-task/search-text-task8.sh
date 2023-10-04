#!/bin/bash

# var
path=""
text=""

# parse arguments with comannd getopts 
while getopts ":p:s:" opt; do
  case "$opt" in
    p) path="$OPTARG";;
    s) text="$OPTARG";;
    \?) echo "Usage: $0 -p <path> -s <text>"; exit 1;;
  esac
done

# check path and text are provided
if [ -z "$path" ] || [ -z "$text" ]; then
  echo "Both path and text are required arguments. Use -p for path and -s for text."
  exit 1
fi

# check directory
if [ ! -d "$path" ]; then
  echo "The specified path is not a directory: $path"
  exit 1
fi

# search for files containing the specified text in the directory
found_files=$(grep -rl "$text" "$path")

# output
if [ -z "$found_files" ]; then
  echo "No files containing '$text' found in '$path'."
else
  echo "Files containing '$text' in '$path':"
  echo "$found_files"
fi
