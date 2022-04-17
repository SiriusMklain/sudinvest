from django.shortcuts import render, redirect
from forms.forms import *


def home(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    context  = {
        'form': form,
        'form_lite': form_lite
    }
    return render(request, 'staticpage/home.html', context=context)


def about(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    context = {
        'form': form,
        'form_lite': form_lite
    }
    return render(request, 'staticpage/about.html', context=context)


def info(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    context = {
        'form': form,
        'form_lite': form_lite
    }
    return render(request, 'staticpage/info.html', context=context)


def investments(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    context = {
        'form': form,
        'form_lite': form_lite
    }
    return render(request, 'staticpage/investments.html', context=context)


def vziskaniye(request):
    form = FeedBackForm(request.POST)
    form_lite = FeedBackLite(request.POST)
    context = {
        'form': form,
        'form_lite': form_lite
    }
    return render(request, 'staticpage/vziskaniye.html', context=context)
