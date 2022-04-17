from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view'),
    path('', FeedBackViewLite.as_view(), name='feedback_view_lite'),
    path('feedback_success/', feedback_success, name='feedback_success')
]
