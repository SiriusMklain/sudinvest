from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail
from django.template import Template
from django.core.mail import get_connection, EmailMultiAlternatives


def send_message(name, email, phone):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'phone': phone}
    subject = 'Сообщение с сайта investsud'
    from_email = 'dev@makarenko.tech'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['sergeimakarenko5991@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


class MessageForm(View):
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
                    return redirect('forms_success')
                else:
                    print('error_message')
        else:
            form = FeedBackForm()


class MessageLite(View):
    def post(self, request):
        if request.method == 'POST':
            form = FeedBackLite(request.POST)
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
                    return redirect('forms_success')
                else:
                    print('error_message')
        else:
            form = FeedBackLite()




def forms_success(request):
    return render(request, 'forms/feedback_success.html')

