from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail


class FeedBackViewLite(View):
    def post(self, request):
        if request.method == 'POST':
            form_lite = FeedBackLite(request.POST)
            if form_lite.is_valid():
                form.save()
                message = '<ul>' \
                          '<li>' + form.cleaned_data['name'] + '</li>' \
                          '<li>' + form.cleaned_data['phone'] + '</li>' \
                          '<li>' + form.cleaned_data['email'] + '</li>' \
                          '</ul>'
                mail = send_mail(form.cleaned_data['name'], message, 'dev@makarenko.tech',
                                 ['sergeimakarenko5991@gmail.com'], fail_silently=False)
                if mail:
                    print('success_message')
                    form_lite.save()
                    return redirect('feedback_success')
                else:
                    print('error_message')


class FeedBackView(View):
    def post(self, request):
        if request.method == 'POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                message = '<ul>' \
                          '<li>' + form.cleaned_data['name'] + '</li>' \
                          '<li>' + form.cleaned_data['phone'] + '</li>' \
                          '<li>' + form.cleaned_data['email'] + '</li>' \
                          '</ul>'
                mail = send_mail(form.cleaned_data['name'], message, 'dev@makarenko.tech',
                                 ['sergeimakarenko5991@gmail.com'], fail_silently=False)
                if mail:
                    print('success_message')
                    form.save()
                    return redirect('feedback_success')
                else:
                    print('error_message')




def feedback_success(request):
    return render(request, 'feedback/feedback_success.html')
