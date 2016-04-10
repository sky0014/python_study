# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000
# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：
# by sky0014


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


if __name__ == '__main__':
    L = range(1, 1000)
    print(list(filter(is_palindrome, L)))
