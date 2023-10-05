import yaml
from yaml.loader import SafeLoader

FILE_NAME = 'test_file.yaml'


def read_file():
    with open(FILE_NAME) as f:
        data = yaml.load(f, Loader=SafeLoader)
        return data


def main():
    data = read_file()
    for keys, values in data.items():
        if keys == 'passwords':
            for value in values:
                for name, password in value.items():
                    print(password)

if __name__=="__main__":
    main()
