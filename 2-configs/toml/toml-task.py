import tomllib
import sys
import os

FILE_NAME = 'test.toml'


def file_exist():
    path = os.path.join(os.getcwd(), FILE_NAME)
    if os.path.exists(path):
        return True


def read_toml_file(file):
    try:
        with open(file, "rb") as f:
            data = tomllib.load(f)
        return data
    except Exception as e:
        print("Can't read a file \n{}".format(e))
        sys.exit()


def main():
    if file_exist():
        text = read_toml_file(FILE_NAME)
        for info, user in text.items():
            for key, value in user.items():
                if key == 'password':
                    print(value)


if __name__ == '__main__':
    main()
