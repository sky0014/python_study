# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# by sky0014

from functools import reduce

dot = False
dotn = 0


def convert(x, y):
    global dot
    global dotn
    if y == '.':
        dot = True
        return x

    if dot:
        dotn -= 1
        return x + y * 10**dotn
    else:
        return x * 10 + y


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
            '9': 9,
            '.': '.'}[s]


def str2float(s):
    return reduce(convert, map(char2num, s))


if __name__ == '__main__':
    print(str2float('1234.5678'))
