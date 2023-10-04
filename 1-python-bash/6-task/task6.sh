#!/bin/bash

 if [ "$#" -ne 2 ]; then
    echo "Використання: $0 <шлях_до_директорії> <текст_для_пошуку>"
    exit 1
fi

directory="$1"
search_text="$2"

if [ ! -d "$directory" ]; then
    echo "Директорія '$directory' не існує."
    exit 1
fi

found_files=$(grep -rl "$search_text" "$directory")

if [ -z "$found_files" ]; then
    echo "Файли, що містять текст '$search_text', не знайдено у директорії '$directory'."
else
    echo "Файли, що містять текст '$search_text' у директорії '$directory':"
    echo "$found_files"
fi

