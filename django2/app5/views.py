from django.shortcuts import render
from app5.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            num1=data1.get("num1")
            result=square(num1)
            return render(request,'app5/index.html',{'param1':result})
    else:
        form1=inputform()
    return render(request,'app5/index.html',{'form':form1})

def square(num1):
    return num1*num1