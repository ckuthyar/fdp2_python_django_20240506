from django.shortcuts import render
from app5.forms import inputweb
import datetime as dt
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            city1=data1.get("city1")
            if city1=="BLR":
                result=getTime1()
            else:
                result=getTime2()
            return render(request,'app5/index.html',{'param1':result,"form":form1})
    else:
        form1=inputweb()
        result=getTime1()
    return render(request,'app5/index.html',{'param1':result,"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
def getTime1():
    today=dt.datetime.now()
    y1=today.year
    m1=today.month
    d1=today.day
    h1=today.hour
    M1=today.minute
    result=str(y1)+"-"+str(m1).zfill(2)+"-"+str(d1).zfill(2)+" "+str(h1).zfill(2)+":"+str(M1).zfill(2)
    return result

def getTime2():
    today=dt.datetime.now()
    diff=dt.timedelta(hours=5.5+7)
    today=today-diff
    y1=today.year
    m1=today.month
    d1=today.day
    h1=today.hour
    M1=today.minute
    result=str(y1)+"-"+str(m1).zfill(2)+"-"+str(d1).zfill(2)+" "+str(h1).zfill(2)+":"+str(M1).zfill(2)
    return result