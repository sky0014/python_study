# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431821084171d2e0f22e7cc24305ae03aa0214d0ef29000
# 求素数
# by sky0014


def odd_iter():
    i = 3
    while True:
        yield i
        i += 2


def can_div(n):
    return lambda x: x % n > 0


def primes():
    a = 2
    L = odd_iter()
    while True:
        yield a
        L = filter(can_div(a), L)
        a = next(L)


if __name__ == '__main__':
    for prime in primes():
        if (prime > 1000):
            break
        else:
            print(prime)
