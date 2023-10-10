import yaml
from yaml.loader import SafeLoader
import logging

FILE_NAME = 'test_file.yaml'
keywords = ('password', 'passwords', 'pass')
logger = logging.getLogger()


def show_info(*args):
    logging.basicConfig(level=logging.INFO)
    return logger.info(str(args))


def read_file():
    with open(FILE_NAME) as f:
        return yaml.load(f, Loader=SafeLoader)


def main():
    data = read_file()
    values = []
    for keys, info in data.items():
        for word in keywords:
            if keys == word:
                for i in info:
                    for key, value in i.items():
                        values.append(value)
            else:
                if hasattr(info, '__iter__'):
                    for i in info:
                        for key, value in i.items():
                            if key == word:
                                values.append(value)
    show_info(values)


main()import yaml
from yaml.loader import SafeLoader
import logging

FILE_NAME = 'test_file.yaml'
keywords = ('password', 'passwords', 'pass')
logger = logging.getLogger()


def show_info(*args):
    logging.basicConfig(level=logging.INFO)
    return logger.info(str(args))


def read_file():
    with open(FILE_NAME) as f:
        return yaml.load(f, Loader=SafeLoader)


def main():
    data = read_file()
    values = []
    for keys, info in data.items():
        for word in keywords:
            if keys == word:
                for i in info:
                    for key, value in i.items():
                        values.append(value)
            else:
                if hasattr(info, '__iter__'):
                    for i in info:
                        for key, value in i.items():
                            if key == word:
                                values.append(value)
    show_info(values)


main()
