import os
import json

FILE_NAME='config.json'

def main():
    file_path = os.path.join(os.getcwd(), FILE_NAME)
    if not os.path.isfile(file_path):
        print(f'{FILE_NAME} not found in current directory')
    else:
        with open(FILE_NAME, 'r') as f:
            config = json.load(f)
        if 'password' not in config:
            print(f'{FILE_NAME} does not contain filed \'password\'')
        else:
            print(config['password'])
    
if __name__=="__main__":
    main()
