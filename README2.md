# Django Project Creation Proc**edure Document
## Database tables are created in Django's SQLite
### Author: CS, Sivashankar

**Assignment4 - Student Course Registration** - Take 3 inputs - student name, college name and course name. These should be stored inside the SQLite database. Admin should be able to see the list of students registered for the course

#### >django-admin startproject django2
#### >cd django2
#### >django-admin startapp app1


In **app1/models.py**
```
from django.db import models
class students(models.Model):
    name1=models.CharField(max_length=50)
    college1=models.CharField(max_length=100)
    course1=models.CharField(max_length=30)
```

In **app1/forms.py** and add
```
from django import forms
from app1.models import students
class inputform(forms.ModelForm):
    class Meta:
        model=students
        fields=['name1','college1','course1']
```

In **app1/views.py**
```
from django.shortcuts import render
from app1.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()  //save to database
            return render(request,'app1/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'app1/index.html',{'form':form1})
```


In tempates/app1/index.html
```
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Submit</button>
    </form>
    <p>{{param1}}</p>
```


#### >python manage.py makemigrations
#### >python manage.py migrate

#### http://127.0.0.1:8080/app1       
#### >python manage.py createsuperuser   
#### http://127.0.0.1:8080/admin

In **app1/models.py** - Within the class, add a function, so that the object name is the same as the student's name
```
def __str__(self):
    return self.name1
```
        
In **app1/admin.py**
```
from .models import students
admin.site.register(students)
```

We can also check by clicking on db.sqlite
Install SQLite Viewer extension in VSCode

**Assignment5 - Create Online Account Opening form for ICICI Bank** Take 4 inputs - First Name, Last Name, Aadhaar, Pincode. Create an auto-incremented Account Number starting from 8000.
#### >django-admin startapp app2


In **app2/models.py**
```
from django.db import models
class bank1(models.Model):
    fname1=models.CharField(max_length=50)
    lname1=models.CharField(max_length=100)
    aadhar1=models.IntegerField(max_length=12)
    pincode1=models.IntegerField(max_length=6)
```

In **app2/forms.py** and add
```
from django import forms
from app2.models import bank1
class inputform(forms.ModelForm):
    class Meta:
        model=bank1
        fields=['fname1','lname1','aadhar1','pincode1']
```

In **app2/views.py**
```
from django.shortcuts import render
from app2.forms import inputform

def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            form1.save()  //save to database
            return render(request,'app2/index.html',{'form':form1,'param1':"Success"})
    else:
        form1=inputform()
    return render(request,'app2/index.html',{'form':form1})
```


In tempates/app2/index.html
```
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">Submit</button>
    </form>
    <p>{{param1}}</p>
```


#### >python manage.py makemigrations
#### >python manage.py migrate

#### http://127.0.0.1:8080/app2    
#### >python manage.py createsuperuser  

Provide username - eg admin   
Provide email address - eg user1@gmail.com  
Provide password - *When you enter the password, you will not be able to see any character on the console. However, your entry will be accepted by the system. If password rule is not followed, you can override by clicking **y***   
#### http://127.0.0.1:8080/admin

In **app2/models.py** - Within the class, add a function, so that the object name is the same as the student's name
```
def __str__(self):
    return self.name1
```
        
In **app2/admin.py**
```
from .models import students
admin.site.register(students)
```
We can also check by clicking on db.sqlite

