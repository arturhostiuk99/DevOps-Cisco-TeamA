import tomllib
import logging
import sys
import os

FILE_NAME = 'test.toml'
keywords = ['password', 'passwords', 'pass']
logger = logging.getLogger()


def file_exist():
    path = os.path.join(os.getcwd(), FILE_NAME)
    if os.path.exists(path):
        return True


def read_toml_file(file):
    try:
        with open(file, "rb") as f:
            return tomllib.load(f)
    except Exception as e:
        print("Can't read a file \n{}".format(e))
        sys.exit()


def show(*args):
    logging.basicConfig(level=logging.INFO)
    return logger.info(str(args))


def main():
    if file_exist():
        text = read_toml_file(FILE_NAME)
        values = []
        for word in keywords:
            for info, user in text.items():
                if info == word:
                    for key, value in user.items():
                        values.append(value)
                else:
                    for key, value in user.items():
                        if key == word:
                            values.append(value)
        show(values)


if __name__ == '__main__':
    main()
