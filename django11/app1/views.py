from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def landing(request):
    return render(request,'app1/landing.html')	

def home(request):
    return render(request,'app1/home.html')	

def Sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'app1/index.html',{'form':form, 'error_message': form.errors.get('__all__')})
    else:
        form=UserCreationForm()
    return render(request,'app1/index.html',{'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                return render(request,'app1/home.html',{'param1':form})
        return render(request, 'app1/index.html', {'form': form, 'error_message': form.errors.get('__all__')})
    else:
        form = AuthenticationForm()
    return render(request, 'app1/index.html', {'form': form})

def home(request):
    return render(request,'app1/index.html',{'param1':"hello world"})

# Create your views here.
