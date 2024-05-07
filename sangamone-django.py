import os
dproject=input("Enter the django project name: ")
dapp=input("Enter the django app name: ")

os.chdir(dproject)             # Changing path to django folder
os.chdir(f"./{dproject}")      # Entering inside the project file
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
else:
    any1=info1.replace("path('admin/', admin.site.urls),",f"""path('admin/', admin.site.urls),\n\tpath("{dapp}/" ,include("{dapp}.urls")),""")
    f1.seek(0)
    f1.write(any1)
f1.close()

os.chdir(f"../{dapp}")        # Navigationg to app folder
f1=open("views.py","w")       
any="""from django.shortcuts import render
def home(request):
    return render(request,'"""+dapp+"""/index.html',{'param1':"hello world"})"""
f1.write(any)
f1.close()

open('urls.py','w')          # Creating urls.py inside the app folder
f1=open("urls.py","r+")
if "urlpatterns = [" not in f1.read():
    f1.write(f"from django.urls import path\nfrom {dapp}.views import home\nurlpatterns = [\n\tpath('', home),]")
else:
    a=f1.read().replace("urlpatterns = [",f"urlpatterns = [\n\tpath('', home),").replace("from django.urls import path",f"from django.urls import path\nfrom {dapp}.views import home")
    f1.seek(0)
    f1.write(a)
f1.close()


os.makedirs(f"templates/{dapp}")     # Creating templates folder for index.py 
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
    <p>Hello World</p>
    <p>{{param1}}</p>
</body>
</html>
""")
f1.close()

