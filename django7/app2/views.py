from django.shortcuts import render
def home(request):
    return render(request,'app2/index.html',{'param1':"DSU Campus, Harohalli"})

# Create your views here.
