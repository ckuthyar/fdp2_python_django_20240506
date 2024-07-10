import os
dir1="D:/Sample/"
list1=list(os.listdir(dir1))
list2=[]
list3=[]

for i in list1:
    if os.path.isfile(dir1+i):
        list2.append(i)
    else:
        list3.append(i)
print(list2)
print(list3)
