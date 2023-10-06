import configparser
import os


path_to_ini = 'config.ini'
search_key = 'password'


def exist_ini(exists_ini):
    if not os.path.exists(exists_ini):
        return True


def search_pass(file_ini, param):
    config = configparser.ConfigParser()
    config.read(file_ini)
    sections = config.sections()
    passwords = []
    for section in sections:
        for key in config[section]:
            if key == param:
                passwords.append(config.get(section, key))
    return print(passwords)


def run_script():
    if exist_ini(path_to_ini):
        return print(f'{path_to_ini} doesnt not exists')
    search_pass(path_to_ini, search_key)


run_script()
