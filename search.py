import sys
import os

__author__ = 'wangxingwei'


def search_path(file_name, path):
    print('searching ... %s' % path)
    for p in os.listdir(path):
        if file_name in p:
            print(os.path.abspath(p))
        elif os.path.isdir(p):
            search_path(file_name, p)


if __name__ == '__main__':
    file_name = sys.argv[1]
    search_path(file_name, 'c:')
