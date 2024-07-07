from django.shortcuts import render
from app1.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        print("where are u")
        if form1.is_valid():
            data=form1.cleaned_data
            print(data)
            n1=data.get('input1')
            name1=data.get('input2')
            result=n1*n1
            return render(request,'app1/index.html',{
                'param1':result,
                'param2':name1,
                'form':form1

            })
    else:
        form1=inputform()
    return render(request,'app1/index.html',{'form':form1
    })

