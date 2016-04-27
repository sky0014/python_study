def consumer():
    r = 'yoyo'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s ...' % n)
        r = '200 OK'


def produce(c):
    print(c.send(None))
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s ...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer returns %s' % r)
    c.close()


c = consumer()
produce(c)
