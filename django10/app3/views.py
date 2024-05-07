from django.shortcuts import render
def home(request):
    list1=[]
    for i in range(0,10,2):
        list1.append(i)
    return render(request,'app3/index.html',{'param1':list1})