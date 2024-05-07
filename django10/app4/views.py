from django.shortcuts import render
def home(request):
    month1=4
    list1=[31,29,31,30,31,30,31,31,30,31,30,31]
    s2=""
    week=["wed","thu","fri","sat","sun","mon","tue"]
    list2=[]
    list3=[]    
    days1=list1[month1]
    for i in range(0,days1,1):
        list2.append(i)
    len2=len(list2)
    count=(7*5)-len2
    for i in range(0,count,1):
        list2.append(i)   
    for i in range(0,7,1):
        s2=s2+week[i]+" "
    for j in range(0,5,1):
        s1=""
        for i in range(7*j,7*(j+1),1):
            s1=s1+str((list2[i]%31)+1).zfill(3)+" "
        list3.append(s1)
    return render(request,'app4/index.html',{'param1':s2,'param2':list3})