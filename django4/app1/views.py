from django.shortcuts import render
from app1.forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n=data1.get("num1")
            result=square(n)
            return render(request,'app1/index.html',{'param1':result,'param2':n,"form":form1})
    else:
        form1=inputweb()
    return render(request,'app1/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
def square(n):
    return n*n