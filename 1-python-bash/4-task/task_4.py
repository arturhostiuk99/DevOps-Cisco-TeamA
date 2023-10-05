import argparse
import os

parser = argparse.ArgumentParser(description='Problem 4 with two arguments')

parser.add_argument('-p', '--path', help='Search path')
parser.add_argument('-s', '--string', help='The string you need to find')

args = parser.parse_args()


def availability_parse_args(path, string):
    """This function checks if arguments were provided when running the python script"""
    if not path and not string:
        print(f'You need to specify the path and a string to search for')
        exit()
    elif not string:
        print(f'You need to specify a string to search for')
        exit()
    elif not path:
        print(f'You need to specify the path')
        exit()

availability_parse_args(args.path, args.string)
print("Search...")


def return_files(preset_path, search_string):
    """This function searches the directories that are in the path,
    searches all files and checks whether the given line is present in the file"""
    files = []
        def list_files(list_files, files):
        try:
            with open(list_files, 'r') as f:
                if search_string in f.read():
                    files.append(list_files)
        except Exception as e:
            return f'Error reading file {list_files}: {str(e)}'
    if os.path.isdir(preset_path):
        for dir_path, dir_names, filenames in os.walk(preset_path):
            for filename in filenames:
                file_path = os.path.join(dir_path, filename)
                list_files(file_path,files)
    elif os.path.isfile(preset_path):
        list_files(preset_path,files)
    return print(files)


return_files(args.path, args.string)
