# Bash Script for Searching Text in Files - Task #8 BASH 

This Bash script allows you to search for files containing specific text within a directory. You can use it to quickly find files that match a particular search criteria. This guide will walk you through the steps to use the script effectively.

## Usage

1. Navigate to the script directory.
```bash
cd <name script dir>
```

2. Make the script executable:
```bash
chmod +x search-text-task8.sh
```

3. The script accepts two arguments:

`-p:` The `path` to the directory you want to search within. \
`-s:` The `text` you want to search for in the files.
Here's the basic usage of the script:
```bash
./search-text-task8.sh -p /path/to/search/directory -s "text_to_search"
```

Replace `/path/to/search/directory` with the directory where you want to search for files. \
Replace `"text_to_search"` with the text you want to search for within those files

Let's say you want to search for files containing the word "softserve" within the directory `~/softserve-academy directory`. You would use the script like this:
```bash
./search-text-task8.sh -p ~/softserve-academy -s softserve
```
Output:
```bash
Files containing 'softserve' in '/Users/macbookair/softserve-academy':
/Users/macbookair/softserve-academy/test4.txt
/Users/macbookair/softserve-academy/test2.txt
/Users/macbookair/softserve-academy/test3.txt
```

The script will provide you with the list of files that contain the specified text in the given directory. If no matching files are found, it will display a message indicating that no files were found.

