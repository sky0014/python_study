import asyncio


@asyncio.coroutine
def hello():
    print('hello there!')
    yield from asyncio.sleep(1)
    print('hello again! ')


@asyncio.coroutine
def wget(host):
    print('wget %s ...' % host)
    reader, writer = yield from asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    print('\r\n')
    writer.close()


loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.run_until_complete(
    asyncio.wait([wget(host) for host in ['www.sohu.com', 'www.sina.com', 'www.163.com', 'www.baidu.com']]))
loop.close()
