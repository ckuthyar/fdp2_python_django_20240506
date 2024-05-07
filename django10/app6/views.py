from django.shortcuts import render
def home(request):
    import datetime as dt
    today = dt.datetime.now()
    list1 = []
    h1 = today.hour
    m1 = today.minute
    s1 = today.second

    list1.append(h1)
    list1.append(m1)
    list1.append(s1)
    return render(request,'app6/index.html',{'param1':list1})