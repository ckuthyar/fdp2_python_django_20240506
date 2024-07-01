from django.shortcuts import render
def home(request):
    dict1={}
    for i in range(1,5,1):
        dict1[i]=fact(i)
    print(dict1)

    dict2={'India':'New Delhi','USA':'Washington DC','UK':'London'}
    return render(request,'app1/index.html',{'param1':dict1, 'param2':dict2})

def square(num1):
    return num1*num1
def fact(num1):
    fact1=1
    for i in range(1,num1+1,1):
        fact1=fact1*i
    return fact1
