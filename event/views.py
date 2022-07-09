from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Birth, Death, Divorce, Marriage



def home(request):
    return render(request, 'event/home.html')

@login_required(login_url='login')
def birth(request):
    queryset = Birth.objects.all()
    return render(request, 'event/birth.html', {'births': queryset})

@login_required(login_url='login')
def death(request):
    queryset = Death.objects.all()
    return render(request, 'event/death.html', {'deaths': queryset})

@login_required(login_url='login')
def marriage(request):
    queryset = Marriage.objects.all()
    return render(request, 'event/marriage.html', {'marriages': queryset})

@login_required(login_url='login')
def divorce(request):
    queryset = Divorce.objects.all()
    return render(request, 'event/divorce.html', {'divorces': queryset})


def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exist')              
    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password is incorrect')              


    return render(request, 'event/login_form.html')


def logout_page(request):
    logout(request)
    return redirect('home')
       
    