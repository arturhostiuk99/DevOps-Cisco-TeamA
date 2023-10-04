import os
from sys import argv


def check_if_path_is_None():
    try:
        path = argv[1]
        if path == '':
            print('Your path is empty')
            return False
        return True
    except IndexError:
        print("You don't input path")
        return False


def check_if_file_extension_is_None():
    try:
        file_extension = argv[2]
        if file_extension == '':
            print('Your file_extension is empty')
            return False
        return True
    except IndexError:
        print("You don't input file extension")
        return False


def check_if_path_exist(path):
    """This boolean function is checking if the input path is exist."""
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                raise ValueError
            elif os.path.isdir(path):
                return True
    except ValueError:
        print("Incorrect path or final path is a file")
        return False


def all_validation():
    if check_if_path_is_None():
        if check_if_file_extension_is_None():
            if check_if_path_exist(argv[1]):
                return True
