import os
from sys import argv
from validation import all_validation


def main():
    """Input the path and file extension and get a names of files in final directory"""
    if all_validation():
        print('The given path: {} \nThe given file extension: {}'.format(argv[1], argv[2]))
        for files in os.listdir(argv[1]):
            if files.endswith(argv[2]):
                print('The file name: {}'.format(files))


if __name__ == "__main__":
    main()
