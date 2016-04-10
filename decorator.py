# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000
# 装饰器学习
# by sky0014

from functools import wraps


def log(text):
    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kw):
            print('%s begin call %s' % (text, func.__name__))
            result = func(*arg, **kw)
            print('%s end call %s' % (text, func.__name__))
            return result
        return wrapper
    return decorator


@log('decorator')
def now():
    print('2016-4-11')
    return 'return test'


def main():
    print(now())
    print(now.__name__)


if __name__ == '__main__':
    main()
