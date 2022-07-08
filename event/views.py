from django.shortcuts import render
from . models import Birth, Death, Divorce, Marriage
# Create your views here.


def home(request):
    return render(request, 'event/home.html')


def birth(request):
    queryset = Birth.objects.all()
    return render(request, 'event/birth.html', {'births': queryset})


def death(request):
    queryset = Death.objects.all()
    return render(request, 'event/death.html', {'deaths': queryset})


def marriage(request):
    queryset = Marriage.objects.all()
    return render(request, 'event/marriage.html', {'marriages': queryset})


def divorce(request):
    queryset = Divorce.objects.all()
    return render(request, 'event/divorce.html', {'divorces': queryset})
