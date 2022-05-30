from django.urls import path
from .views import *

urlpatterns = [
#    path('', FeedBackView.as_view(), name='feedback_view'),
#     path('', MessageLite.as_view(), name='feedback_view_lite'),
    path('test/', MessageForm.as_view(), name='feedback_view'),
    # path('form/', forms_success, name='forms_success')
]
