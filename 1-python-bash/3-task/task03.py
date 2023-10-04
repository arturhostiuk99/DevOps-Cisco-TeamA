import os


def check_if_config_file_exist():
    """We check whether the file with our script is in the same directory"""
    current_file = os.path.realpath(__file__)  # path to our script file
    current_directory = os.path.dirname(current_file)
    for files in os.listdir(current_directory):
        if files == 'Config.txt':
            return True
    print(
        "Config file doesn't exist, this file create automatically, with the path to this directory and file extension '.txt'")
    with open('Config.txt', "w") as config_file:
        config_file.write(current_directory + '\n')
        config_file.write(".txt")
        return config_file


def check_if_config_file_is_empty():
    """We check whether at least one of the arguments is empty"""
    if check_if_config_file_exist():
        with open('Config.txt', 'r') as config_file:
            data = config_file.read()
            arguments = data.split('\n')
            if data == '' or len(arguments) != 2 or arguments[0] == '' or arguments[1] == '':
                print(
                    'Config file is empty or missing arguments. The file will automatically be filled with the path to this directory and file extension ".txt"')
                current_file = os.path.realpath(__file__)
                current_directory = os.path.dirname(current_file)
                with open('Config.txt', 'w') as config_file:
                    config_file.write(str(current_directory) + '\n')
                    config_file.write(".txt")
                return config_file
            else:
                return True


def check_if_path_exist():
    """This boolean function is checking if the input path is exist."""
    if check_if_config_file_is_empty():
        with open('Config.txt', 'r') as config_file:
            arguments = config_file.read().splitlines()
        try:
            if os.path.exists(arguments[0]):  # check if path in config file exist in os
                if os.path.isfile(arguments[0]):  # check if endpoint of path is file
                    raise ValueError
                elif os.path.isdir(arguments[0]):  # check if endpoint of path is dir
                    return arguments
            else:
                raise ValueError
        except ValueError:
            print("Incorrect path in config file or final path is a file")


def returns_count_of_files():
    """Input the path and file extension and get a number of files in final directory"""
    if check_if_path_exist():
        paths = check_if_path_exist()[0]
        file_extension = check_if_path_exist()[1]
        list_of_files = list()
        for files in os.listdir(paths):  # function os.listdir return only file names in final specified directory
            if files.endswith(file_extension):  # function endswith compares latest values of objects
                list_of_files.append(files)
        print('Numbers of files with extension "{}": {}'.format(file_extension, len(list_of_files)))


if __name__ == "__main__":
    returns_count_of_files()
