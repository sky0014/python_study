# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318230588782cac105d0d8a40c6b450a232748dc854000
# sorted练习
# by sky0014


def by_name(o):
    return o[0]


def by_score(o):
    return o[1]


def main():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    # L2 = sorted(L,key=by_name)
    L2 = sorted(L, key=by_score, reverse=True)
    print(L2)


if __name__ == '__main__':
    main()
