from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('info/', info, name='info'),
    path('investments/', investments, name='investments'),
    path('vziskaniye/', vziskaniye, name='vziskaniye'),
]