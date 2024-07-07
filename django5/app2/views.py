from django.shortcuts import render
from app2.forms import iciciform
# Create your views here.
def home(request):
    if request.method=='POST':
        form1=iciciform(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request,'app2/index.html',{
                'form':form1
            })
    else:
        form1=iciciform()
    return render(request,'app2/index.html',{
                'form':form1
            })