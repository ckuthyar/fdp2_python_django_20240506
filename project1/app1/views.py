from django.shortcuts import render

# Create your views here.
def doctor1(request):
    return render(request,'app1/doctor1.html')

def doctor2(request):
    return render(request,'app1/doctor2.html')

def doctor3(request):
    return render(request,'app1/doctor3.html')

def doctorlayout(request):
    return render(request,'app1/doctorlayout.html')
