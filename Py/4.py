def evenodd(limit):
    
    list1=[]
    list2=[]
    for i in range(0,limit,2):
        list1.append(i)
        list2.append(i+1)
    return (list1,list2)
result=evenodd(20)
print(result[0])
print(result[1])
