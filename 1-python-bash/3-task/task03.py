import os

__paths = input("Input path of final directory:")
__file_extension = input("Input file extension:")


def check_if_path_exist(paths):
    """This boolean function is checking if the input path is exist."""
    try:
        if os.path.exists(paths):  # check if path exist
            if os.path.isfile(paths):  # check if endpoint of path is file
                raise ValueError
            elif os.path.isdir(paths):  # check if endpoint of path is dir
                return True
        else:
            raise ValueError
    except ValueError:
        print("Incorrect path or final path is a file")


def returns_count_of_files(paths: str, file_extension: str):
    """Input the path and file extension and get a number of files in final directory"""
    if check_if_path_exist(paths):
        list_of_files = list()
        for files in os.listdir(paths):  # function os.listdir return only file names in final specified directory
            if files.endswith(file_extension):  # function endswith compares latest values of objects
                list_of_files.append(files)
        print(len(list_of_files))


returns_count_of_files(__paths, __file_extension)
