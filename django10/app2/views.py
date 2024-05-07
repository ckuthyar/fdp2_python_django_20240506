from django.shortcuts import render
def home(request):
    list1=[]
    list2=[]
    for i in range(0,10,2):
        list1.append(i)
        list2.append(i+1)
    return render(request,'app2/index.html',{'param1':list1, 'param2':list2})