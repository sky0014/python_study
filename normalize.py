# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# by sky0014

from functools import reduce


def join(x, y):
    return x + y


def fun(name):
    return reduce(join, [c.upper() if i == 0 else c.lower() 
                         for i, c in enumerate(name)])


def normalize(names):
    return list(map(fun, names))


if __name__ == '__main__':
    print(normalize(['adam', 'LISA', 'barT']))
