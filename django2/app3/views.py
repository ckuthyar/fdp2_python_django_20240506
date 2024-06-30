from django.shortcuts import render
def home(request):
    result=facts(8)
    return render(request,'app3/index.html',{'param1':result})

def fact(num1):
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1

def facts(limit1):
    list1=[]
    for i in range(2,limit1,1):
        list1.append(fact(i))
    return list1
        