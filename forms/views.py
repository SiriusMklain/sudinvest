from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail


class FeedBackView(View):
    def post(self, request):
        if request.method == 'POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                message = '<ul>' \
                          '<li>' + form.cleaned_data['name'] + '</li>' \
                          '<li>' + form.cleaned_data['phone'] + '</li>' \
                          '<li>' + form.cleaned_data['email'] + '</li>' \
                          '<li>' + form.cleaned_data['inn'] + '</li>' \
                          '<li>' + form.cleaned_data['sum'] + '</li>' \
                          '</ul>'
                mail = send_mail(form.cleaned_data['name'], message, 'dev@makarenko.tech',
                                 ['sergeimakarenko5991@gmail.com'], fail_silently=False)
                if mail:
                    print('success_message')
                    form.save()
                    return redirect('feedback_success')
                else:
                    print('error_message')
        else:
            form = FeedBackForm()

class FeedBackViewLite(View):
    def post(self, request):
        if request.method == 'POST':
            form = FeedBack(request.POST)
            if form.is_valid():
                message = '<ul>' \
                          '<li>' + form.cleaned_data['name'] + '</li>' \
                          '<li>' + form.cleaned_data['phone'] + '</li>' \
                          '<li>' + form.cleaned_data['email'] + '</li>' \
                          '<li>' + form.cleaned_data['inn'] + '</li>' \
                          '<li>' + form.cleaned_data['sum'] + '</li>' \
                          '</ul>'
                mail = send_mail(form.cleaned_data['name'], message, 'dev@makarenko.tech',
                                 ['sergeimakarenko5991@gmail.com'], fail_silently=False)
                if mail:
                    print('success_message')
                    form.save()
                    return redirect('feedback_success')
                else:
                    print('error_message')
        else:
            form = FeedBack()


def feedback_success(request):
    return render(request, 'forms/feedback_success.html')
