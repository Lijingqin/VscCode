
from datetime import datetime, timedelta, timezone 
now = datetime.now()
print(now)
print(type(now))
print(now.strftime('%a, %b %d %H:%M'))
print('十个小时后：',now + timedelta(hours=10))

dt = datetime(2019,5,30,00,00)
print(dt)
print(dt.timestamp())

t = 1429417200.0
print(datetime.utcfromtimestamp(t))

import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    now = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')

    tz = int(re.match(r'.+?([+-]\d+)', tz_str).group(1))

    now = now.replace(tzinfo = timezone(timedelta(hours=tz)))

    return now.timestamp()

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

