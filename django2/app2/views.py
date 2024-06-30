from django.shortcuts import render
def home(request):
    num1=6
    result=fact(num1)
    return render(request,'app2/index.html',{'param1':result})

def fact(num1):
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1