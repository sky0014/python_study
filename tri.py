# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
# 输出杨辉三角
# by sky0014


def tri():
    a = [1]
    while True:
        yield a
        a.append(0)
        a = [a[i - 1] + a[i] for i in range(len(a))]


if __name__ == '__main__':
    for a in tri():
        print(a)
        if len(a) == 10:
            break
