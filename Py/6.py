def evenodd():
    list1=[]
    list2=[]
    for i in range(0,10,2):
        list1.append(i)
        list2.append(i+1)
    return (list1, list2)
list3=evenodd()
print(list3[0])
print(list3[1])
