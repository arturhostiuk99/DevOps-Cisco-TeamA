import configparser
import os


path_to_ini = 'config.ini'
search_key = 'password'


def exist_ini(exists_ini):
    if os.path.exists(exists_ini):
        search_pass(exists_ini, search_key)
    else:
        return print(f'file .ini doesnt not exists')


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


exist_ini(path_to_ini)

