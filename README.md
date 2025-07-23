# Django_Procedure
Authors: Yutha Achar,CS,Ramachandra,Sivashankar, Kavya Kulal

**Step 0.1 :** In Terminal - create a project with *folder name* and *project name* as **django1**
```
django-admin startproject django1
```

**Step 0.2 :** - change dirctory to *django1*
```
cd django1
```

**Step 0.3 :** - create an app with *app name* as **app1**
```
django-admin startapp app1  
```


**Step1  :** In **django1/settings.py** add 
```
INSTALLED_APPS = [...,'app1', ]
```
**Step2 :** In **django1/urls.py**  - add *include* in import, add *path* in *urlpatterns* 
```
from django.urls import path,include
```

```
path('app1/',include('app1.urls')),
```
**Step3 :**  Under app1 create new folder **templates**,  Under templates create new folder **app1**, Under app1, create new file **index.html**
```
<body>
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
```


**Step4 :** Go to app1/views.py
```
def home(request):
    return render(request,'app1/index.html',{'param1':"hello world"})
```

**Step5 :** Create new file urls.py in app1 and add
```
from django.urls import path
from app1.views import home
urlpatterns = [path('', home),]
```


**Step6 :** Go to Project folder (django1), In Terminal run,  
```
python manage.py runserver
```  
You will get output as   
Hello World   
hello world  
In Browser,
We should make changes in the server at localhost port 8000 i.e; **127.0.0.1:8000/app1**


**Step7:**    
In views.py    
```
from django.shortcuts import render
def home(request):
    n1=5
    result=fact(n1)
    return render(request,'app1/index.html',{'param1':result,'param2':n1})

def fact(n1):  
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1

```
**Step8 :** - In index.html  
```
<body>
    <p>Hello World</p>
    <p>The factorial of {{param2}} is {{param1}}</p>
</body>
```  

**Step9 :** In Terminal run,  
```
python manage.py runserver
```  
We should get output as *The factorial of 5 is 120*  
----End of Factorial Program in App1-------------- 

**Assignment1 - Create a new Django project and a new app using an automated script in link**
https://github.com/ckuthyar/fdp2_python_django_20240506/blob/main/sangamone-django3.0.py
>py sangamone-django3.0.py project1 app1
This will automatically create/update 5 files
project1/settings.py   
project1/urls.py   
app1/templates/app1/index.html   
app1/views.py   
app1/urls.py   
>py manage.py runserver ...will be auto-executed
http://127.0.0.1:8000/app1 ....will show the output

----End of project1 app1 using Automated Script-----


**Assignment2 - Create app2 which takes "5" as an input in a HTML Form and calculates the Factorial of 5**
>django-admin startapp app2
>Repeat Steps 1,2,3,4,5,6

 **Step10 :** Create new file **app2/forms.py**
```
from django import forms
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=1,max_value=10,label="Enter a number")
```

**Step11 :** in index.html
```
<body>
    <h1>Factorial Program</h1>
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}    
        <button type="submit">find factorial</button>
    </form>
    <p>Factorial of {{param2}} is {{param1}}
    </body>
```  
   
**Step12 :** in app2/views.py, 
```
from django.shortcuts import render
from app2.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=fact(n1)
            return render(request,"app2/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app2/index.html",{'form':form1})
```
```
def fact(n1):  
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1
```
**Step13 :** In Terminal run,  
```
python manage.py runserver
```  
In http://127.0.0.1:8000/app2 we should get *The factorial of 5 is 120*                     
----End of Factorial Program in App2--------------  

**Assignment3: Create app3** to print factorial numbers from 1 to 8, one below the other as shown. Let us return param1=[1,2,6,24,120,720,5040,40320] and param2=[1,2,3,4,5,6,7,8] from views.py and iterate these 2 lists using {% for each %} syntax  
Factorial of 1 - 1   
Factorial of 2 - 2   
Factorial of 3 - 6   
Factorial of 4 - 24   
Factorial of 5 - 120   
Factorial of 6 - 720   
Factorial of 7 - 5040   
Factorial of 8 - 40320
```
django-admin startapp app3
```
>Repeat Steps 1,2,3,4,5,6


In **app3/index.html**
```  
<body>   
  <p>Factorial of Numbers</p>
  {% for i in param1 %}
  <p>{{i}}</p>
  {% endfor %}   
</body>
``` 

In **app3/views.py**, we can zip 2 lists and return to HTML
```
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=getFact(n1)  //get factorial for all numbers upto limit1
            return render(request,"app3/index.html",{'param1':result,'form':form1})
    else:
        form1=inputform() 
    return render(request,"app3/index.html",{'form':form1})
```
```
def fact(n1):  
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1

def getFact(limit1):
    list1=[]
    list2=[]
    for i in range(2,limit1+1,1):
        list1.append(fact(i))
        list2.append(i)
    return zip(list1,list2)
```
In **app3/index.html** 
```
<body>   
  <p>Factorial of Numbers</p>
  {% for i,j in param1 %}
  <p>Factorial of {{j}} - {{i}}</p>
  {% endfor %}   
</body>

```
**Assignment4 - Create app4 using automation script**
https://github.com/ckuthyar/fdp2_python_django_20240506/blob/main/sangamone-django4.py

```
python sangamone-django4.py django1 app4
```
The following files are automatically updated or created
>django1\settings.py
>django1\urls.py
>app1\views.py
>app1\urls.py 
>templates\app4\index.html

## Note1: To display images in HTML   
1. In django1 directory create folder **static**
2. Inside **static** folder create folder **images** 
3. Store all your images in **images** folder
4. In django1/settings.py add in the very beginning 
```
import os
```
5. In django1/settings.py under **STATIC_URL** add 
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
6. In app1/index.html, add
```
{% load static %}
<body>
<img src="{% static 'images/img1.jpg' %}">
</body>
```


## Note2: To add CSS file in HTML   
1. In django1 directory create folder **static**
2. Inside **static** folder create folder **css** 
3. Create **style.css** in **css** folder
4. In django1/settings.py add in the very beginning
```
import os
```
5. In django1/settings.py under **STATIC_URL** add 
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```
6. In app1/index.html, add
```
{% load static %}
<body>
<link rel="stylesheet" href="{% static 'style.css' %}">
</body>
```

## Note3: Use HttpResponse without creating index.html 

1. In app1/views.py, add
```
from django.http import HttpResponse
 
def home(request):
    result="Hello World"
    return HttpResponse(result)
```
    
    

## Basic Setup for new programmers

1. Testing for sample Python projects, 1.py to 16.py.  We recommend the use of IDLE for building simple Python code.  During installation, please tick the box - Add Path -  This is very important
https://www.python.org/


2. Django installation.  Go to IDLE - File - Path Browser. Check the location where Python is installed. Eg
>cd USERS   
>cd LAPTOP   
>cd AppData     ( This is a hidden folder, but we can go to cmd and change directory)
>cd Local   
>cd Programs   
>cd Python   
>cd Python312   
>cd Scripts   
>pip3 install django   
>pip3 install mysql-connector-python   
>

3. MySQL installation.  Choose MySQL Community (GPL) Downloads and install 2 products
   
a) MySQL Server   
b) MySQL Workbench   
set username=root,  password=root   
### >create database db1
### >create table employee(id bigint auto_increment primary key, name1 varchar(100))
### >insert into employee(name1) values ("Chandra"), ("Siva"), ("Rajani")
### >select * from employee
https://www.mysql.com/downloads/   

4. VS Code Installation
https://code.visualstudio.com/download
Add extension for Python (Python language support) from Microsoft

5. Git, GitHub 
- Download Git for Windows https://git-scm.com/download/win   Carefully complete the elaborate installation procedure consisting of about 10 steps
- Create account in https://github.com/

6. Basic Testing of all Components
- Choose a working directory D:\coding
- Create a sub-directory:  \django.   
So, all your work will be in D:\coding\django  (preferred) OR C:\coding\django

In IDLE
File - New File - 
```
print(8+4)
```
 - save as 1.py in D:\coding\django   Run - Run Module

In VS Code
Open folder D:\coding\django\
Create index.html, type ! and Enter.  You will see a predefined HTML code. Run - Run without Debugging - Chrome 
Create 2.py - 
```
print(8+3) 
```
- save as 2.py in D:\coding\django. Open Terminal (... in top line), New Terminal
> python 2.py

7. If python command is not in the path, set the environment variable by typing env, edit system environment variables, go to Path, edit, add New,  copy the directory path where Python is installed, save.  Close cmd or Terminal. Open again cmd or Terminal.


8. If django-admin command is not in the path, set the environment variable by typing env, edit system environment variables, go to Path, edit, add New,  copy the directory path where Django is installed, save.  Close cmd or Terminal. Open again cmd or Terminal.

To test, 
>python --version
>django-admin

9. Sample Django programs available in  https://github.com/ckuthyar/fdp2_python_django_20240506/

10. Setup procedures in  README.md and README2.md
https://github.com/ckuthyar/fdp2_python_django_20240506/blob/main/README.md
https://github.com/ckuthyar/fdp2_python_django_20240506/blob/main/README2.md

11. Reference Document created by Sivashankar on 07-Aug-2024
https://docs.google.com/document/d/1-r8vQUzOp6e8Xi1kmZAgOPac0CchO9yfNpdIZbY59BI/edit


