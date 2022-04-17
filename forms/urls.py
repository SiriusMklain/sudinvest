from django.urls import path
from .views import *

urlpatterns = [
#    path('', FeedBackView.as_view(), name='feedback_view'),
    path('', lite_message, name='feedback_view_lite'),
    # path('forms/', forms_success, name='forms')
]
