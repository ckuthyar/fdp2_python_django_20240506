import datetime as dt
import pytz
r1=pytz.timezone('Asia/Kolkata')
t1=dt.datetime.now(r1)
t2=t1.strftime("%Y-%m-%d %H:%M:%S %Z %z")
print(t1)
print(t2)
