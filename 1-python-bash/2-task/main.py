import sys
import os


def main(argv):
    if len(argv) < 1:
        print('Input 2 arguments: <path> <text>')
    else:
        path, search_text = argv[0], argv[1]
        dir_content = os.listdir(path)
        files = [os.path.join(path, f) for f in dir_content if os.path.isfile(os.path.join(path, f))]
        match_files = []
        for file in files:
            with open(file, 'r') as f:
                for line in f:
                    if search_text in line:
                        match_files.append(file)
        if len(match_files) > 0:
            print('Text: "' + search_text + '" found in files: ', [f for f in match_files])
        else:
            print('No match found')


if __name__ == "__main__":
    main(sys.argv[1:])
