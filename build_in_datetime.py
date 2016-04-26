import re
from datetime import datetime, timezone, timedelta

now = datetime.now()
print(now)
print(type(now))
print(now.timestamp())

dt = datetime(2015, 12, 30)
print(dt)
print(dt.timestamp())
print(dt.fromtimestamp(now.timestamp()))
print(dt)

cday = datetime.strptime('2016-01-7', '%Y-%m-%d')
print(cday)

print(now - cday)
print(type(now - cday))

bj = timezone(timedelta(hours=8), 'Beijing')
utc = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc)
print(utc.astimezone(bj))


def to_timestamp(date, zone):
    m = re.match(r'UTC([+-]\d{1,2}):(\d{2})', zone)
    if m:
        ho = int(m.group(1))
        mi = int(m.group(2))
        return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').replace(
            tzinfo=timezone(timedelta(hours=ho, minutes=mi))).timestamp()
    return None


dstr = '2015-6-1 08:10:30'
zstr = 'UTC+7:00'
print('convert %s,%s to %d' % (dstr, zstr, to_timestamp(dstr, zstr)))
