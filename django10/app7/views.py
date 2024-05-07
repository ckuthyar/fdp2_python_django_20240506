from django.shortcuts import render
def home(request):
   
    s1="MGM Collge"
    s2="Indian Society For Technical Education"
    s3="Faculty Chapter KA-118"
   

    return render(request,'app7/index.html',{'param1':s1,'param2':s2,'param3':s3})