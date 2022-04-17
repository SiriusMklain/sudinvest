from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail
from django.template import Template
from django.core.mail import get_connection, EmailMultiAlternatives



def lite_message(request):
    if request.method == 'POST':
        form = FeedBackLite(request.POST)
        if form.is_valid():
            send_message(
                form.cleaned_data['name'],
                form.cleaned_data['email'],
                form.cleaned_data['phone'])
            #return success
            form.save()
    else:
        form = FeedBackLite()
    #context['form'] = form
    return render(request, 'forms/feedback_success.html')

# def success(request):
#     return render(request, 'forms/feedback_success.html', context = context)

def send_message(name, email, phone):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'phone': phone}
    subject = 'Сообщение с сайта investsud'
    from_email = 'dev@makarenko.tech'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['sergeimakarenko5991@gmail.com'])
    msg.attach_alternative(html_content, 'text/ht,l')
    msg.send()