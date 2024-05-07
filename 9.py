
list1=[31,29,31,30,31,30,31,31,30,31,30,31]
s1=""
s2=""
week=["wed","thu","fri","sat","sun","mon","tue"]
list2=[]
month1=4
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
    for i in range(7*j,7*(j+1),1):
        s1=s1+str((list2[i]%31)+1).zfill(3)+" "
    s1=s1+"\n"
print(s2)
print(s1)



    

    
