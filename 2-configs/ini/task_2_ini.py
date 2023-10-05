import configparser

config = configparser.ConfigParser()
config.read('config.ini')

password_value = config.get("keys", "password")

print(password_value)
