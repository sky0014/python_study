# 字符串转换为整数
# by sky0014

from functools import reduce


def char2num(s):
    return {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9}[s]


def add(x, y):
    return x * 10 + y


def int2(s):
    return reduce(add, map(char2num, s))


if __name__ == '__main__':
    print(int2('345555552'))
