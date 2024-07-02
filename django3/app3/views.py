from django.shortcuts import render
import json

def home(request):
    result=quiz1()
    return render(request,'app3/index.html',{'param1':result})


def quiz1():
    f1=open("capitals.json","r")
    data=json.load(f1)
    list1=list(data.keys())
    list2=list(data.values())
    responses=[]
    marks=[]
    s1="What is the capital of "
    s2="?"
    s3="The capital of "
    s4=" is "
    s5="You have scored marks of"
    question=s1+list1[0]+s2
    return question
