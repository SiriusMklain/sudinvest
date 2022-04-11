from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view'),
    path('feedback_success/', feedback_success, name='feedback_success')
]
