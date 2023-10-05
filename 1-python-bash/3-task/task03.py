import os
from sys import argv
from validation import all_validation


def main():
    """Input the path and file extension and get a number of files in final directory"""
    if all_validation():
        list_of_files = list()
        for files in os.listdir(argv[1]):  # function os.listdir return only file names in final specified directory
            if files.endswith(argv[2]):  # function endswith compares latest values of objects
                list_of_files.append(files)
        print('Numbers of files with extension "{}": {}'.format(argv[2], len(list_of_files)))


if __name__ == "__main__":
    main()
