import sys
import subprocess
import os

if len(sys.argv)!=3:
    print("Invalid Cammand: py sangamone-django4.py project_name app_name")
    sys.exit(0)
    

list1=[]

for i in range(1,3):
    list1.append(sys.argv[i])

dproject=list1[0]
dapp=list1[1]
try:
    subprocess.run(['django-admin','startproject',f'{list1[0]}'])
except:
    pass
os.chdir(dproject)
os.chdir(f"./{dproject}")
f1=open("settings.py","r+")
info1=f1.read()
if f"{dapp}'," not in info1:
    a=info1.replace("'django.contrib.staticfiles',",f"'django.contrib.staticfiles',\n\t'{dapp}',")
    f1.seek(0)
    f1.write(a)
f1.close()

f1=open("urls.py","r+")
info1=f1.read()
if f"{dapp}.urls" not in info1 and "from django.urls import path,include" not in info1:
    any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""").replace("from django.urls import path","from django.urls import path,include")
    f1.seek(0)
    f1.write(any1)
elif f"{dapp}.urls" not in info1:
    any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
    f1.seek(0)
    f1.write(any1)
# else:
#     any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
#     f1.seek(0)
#     f1.write(any1)
f1.close()

try:
    os.chdir('../')
    subprocess.run(['django-admin','startapp',f'{list1[1]}'])
except:
    pass

os.chdir(f"{dapp}")

f1=open("forms.py","w")
any="""from django import forms

class inputweb(forms.Form):
    num1=forms.IntegerField(min_value=2,max_value=100,label="Enter Number")
"""
f1.write(any)
f1.close()

f1=open("views.py","w")
any="""from django.shortcuts import render
from """+dapp+""".forms import inputweb
def home(request):
    if request.method=="POST":
        form1=inputweb(request.POST)
        if form1.is_valid():
            data1=form1.cleaned_data
            n=data1.get("num1")
            fact1=factorial1(n)
            return render(request,'"""+dapp+"""/index.html',{'param1':fact1,'param2':n,"form":form1})
    else:
        form1=inputweb()
    return render(request,'"""+dapp+"""/index.html',{"form":form1})

def factorial1(n):
    fact1=1
    for i in range(n,0,-1):
        fact1=fact1*i
    return fact1
"""
f1.write(any)
f1.close()

open('urls.py','w')
f1=open("urls.py","r+")
if "urlpatterns = [" not in f1.read():
    f1.write(f"from django.urls import path\nfrom {dapp}.views import home\nurlpatterns = [\n\tpath('', home),]")
else:
    a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
    f1.seek(0)
    f1.write(a)
# else:
#     for i in range(1,100,1):
#         if f"/{i}" in f1.read():
#             continue
#         else:
#             a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('{i}', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
#             f1.seek(0)
#             f1.write(a)
#             break
f1.close()

try:
    os.makedirs(f"templates/{dapp}")
except:
    pass
os.chdir(f"templates/{dapp}")
f1=open("index.html","w")
f1.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Factorial Calculator</h1>
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <button type="submit">find factorial</button>
    </form>
    <h3> factorial {{param2}} is {{param1}}</h3>
</body>
</html>
""")

f1.close()

os.chdir(f'../../..')
subprocess.run(['python','manage.py','runserver'])