from django.shortcuts import render
import math
def home(request):
    dict1={}
    for i in range(2,8,1):
        dict1[i]=fact(i)
    return render(request,'app2/index.html',{'param1':dict1})

def fact(num1):
    return math.factorial(num1)
