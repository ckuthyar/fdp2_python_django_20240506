from django.shortcuts import render
def home(request):
    return render(request,'app3/index.html',{'param1':"hello world"})