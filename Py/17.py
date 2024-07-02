import json
f1=open("capitals.json","r")
data=json.load(f1)
list1=list(data.keys())
list2=list(data.values())
responses=[]
marks=[]

print("Your Quiz starts now")
s1="What is the capital of "
s2="?"
s3="The capital of "
s4=" is "
s5="You have scored marks of "
for i in range(0,len(list1),1):
    responses.append(input(s1+list1[i]+s2))
print()
for i in range(0,len(list1),1):
    if responses[i]==list2[i]:
        marks.append(10)
    else:
        marks.append(0)
        print(s3+list1[i]+s4+list2[i])
        
print(s5,sum(marks))
    




