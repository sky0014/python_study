import logging
import os
import sys

search_result = []


def search_path(file_name, path):
    # print('searching %s ...' % path)
    try:
        for p in os.listdir(path):
            full_path = os.path.join(path, p)
            if file_name in p:
                search_result.append(full_path)
            elif os.path.isdir(full_path):
                search_path(file_name, full_path)
    except PermissionError as e:
        logging.error(e)


# python search.py Readme d:
if __name__ == '__main__':
    file_name = sys.argv[1]
    path = sys.argv[2]
    search_path(file_name, path)
    for result in search_result:
        print(result)
