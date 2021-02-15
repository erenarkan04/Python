from datetime import datetime, timedelta
import time

print(time.time())

def send_emails():
    for i in range(1000):
        pass

start = time.time()

send_emails()
end = time.time()

print(end - start)

date = datetime(2018, 1, 1)
now = datetime.now()

datetime.strptime("2018/1/1", "%Y/%m/%d")

print(datetime.fromtimestamp(time.time()))

print(f"{date.year}, {date.month}")

duration = date - now
print(duration)

# adds +1 day
date2018 = datetime(2018,1,1) + timedelta(days=1)
print(date2018)