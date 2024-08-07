from django.shortcuts import render
from app5.forms import studentform1

def home(request):
    if request.method=="POST":
        form1=studentform1(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app5/index.html',{'param1':'Successfully inserted','form':form1})
    else:
        form1=studentform1()
    return render(request,'app5/index.html',{'form':form1})