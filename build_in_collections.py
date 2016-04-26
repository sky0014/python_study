import collections
import base64

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

c = collections.Counter('Hello world!')
print(c)


def safe_base64_decode(s):
    n = len(s) % 4
    s += b'=' * n
    return base64.b64decode(s)


print(safe_base64_decode(b'YmluYXJ5AHN0cmluZw'))
