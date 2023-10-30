import configparser
import os


PATH_TO_INI = 'config.ini'
SEARCH_KEY = 'password'


def search_pass(file_ini, param):
    config = configparser.ConfigParser()
    config.read(file_ini)
    sections = config.sections()
    passwords = []
    for section in sections:
        for key in config[section]:
            if key == param:
                passwords.append(config.get(section, key))
    return passwords


def run_script():
    if not os.path.exists(PATH_TO_INI):
        return print(f'{PATH_TO_INI} doesnt not exists')
    print(search_pass(PATH_TO_INI, SEARCH_KEY))


run_script()
