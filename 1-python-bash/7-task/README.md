# File Counter Bash Script - Task #7 BASH 

This Bash script accepts a directory path and a file extension as arguments and returns the number of files with the specified extension in the given directory.

## Usage

1. Navigate to the script directory.
```bash
cd <name script dir>
```

2. Make the script executable:
```bash
chmod +x file-counter-task7.sh
```

3. Run the script with the desired arguments. Replace <directory path> with the path to the directory you want to search and <file extension> with the file extension you're looking for:
```bash
./file-counter-task7.sh <directory path> <file extension>
```
For example, to count the number of .txt files in the ~/softserve-academy directory:
```bash
./file-counter-task7.sh ~/softserve-academy txt
```
The script will display the number of files with the specified extension in the directory.