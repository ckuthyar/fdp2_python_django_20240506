from django.shortcuts import render
from app1.forms import hdfcforms


# Create your views here.
def home(request):
    if request.method == 'POST':
        form1 = hdfcforms(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request ,'app1/index.html', {'form': form1})
    else:
        form1 = i
    return render(request,"app1/index.html",{'form': form1})
