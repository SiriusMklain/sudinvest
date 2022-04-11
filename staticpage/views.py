from django.shortcuts import render
from forms.forms import *


def home(request):
    form = FeedBackForm(request.POST)
    return render(request, 'staticpage/home.html', {'form': form})


def about(request):
    return render(request, 'staticpage/about.html')


def info(request):
    return render(request, 'staticpage/info.html')


def investments(request):
    return render(request, 'staticpage/investments.html')


def vziskaniye(request):
    return render(request, 'staticpage/vziskaniye.html')
