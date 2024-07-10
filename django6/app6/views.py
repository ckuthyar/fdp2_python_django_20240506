from django.shortcuts import render
from app6.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            region1=data1.get("r1")
            result=worldclock2(region1)
            return render(request,'app6/index.html',{'param2':result,"form":form1})
    else:
        form1=inputweb()
        result=worldclock1()
    return render(request,'app6/index.html',{'param1':result,"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
def worldclock1():
    import datetime as dt
    import pytz
    cities=["US/Pacific","US/Eastern","Europe/London",'Asia/Dubai','Asia/Kolkata','Asia/Singapore','Asia/Tokyo','Australia/Sydney']
    times1=[]
    len1=len(cities)
    for i in range(0,len1,1):
        r1=pytz.timezone(cities[i])
        t1=str(dt.datetime.now(r1))
        times1.append(t1+" "+cities[i])
    return times1

def worldclock2(region1):
    import datetime as dt
    import pytz
    r1=pytz.timezone(region1)
    t1=str(dt.datetime.now(r1))
    return t1