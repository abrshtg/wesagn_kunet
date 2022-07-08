from django.shortcuts import render
from . models import Birth, Death, Divorce, Marriage
# Create your views here.


def home(request):
    return render(request, 'event/home.html')


def birth(request):
    queryset = Birth.objects.all()
    return render(request, 'event/birth.html', {'births': queryset})


def death(request):
    return render(request, 'event/death.html')


def marriage(request):
    return render(request, 'event/marriage.html')


def divorce(request):
    return render(request, 'event/divorce.html')
