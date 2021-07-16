import random
import datetime
print(random.randint(1,10000))
now=datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now+datetime.timedelta(days=28))

