from django.shortcuts import render
def home(request):
    import datetime as dt
    today = dt.datetime.now()
    y1 = today.year
    M1 = today.month
    d1 = today.day
    h1 = today.hour
    m1 = today.minute
    s1 = today.second

    str1 = str(y1) + " " + str(M1) + " " + str(d1)
    str2 = str(h1) + " " + str(m1) + " " + str(s1)
    return render(request,'app5/index.html',{'param1':str1, 'param2':str2})