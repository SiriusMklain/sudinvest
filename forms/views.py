from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import View
from django.core.mail import send_mail
from django.template import Template
from django.core.mail import get_connection, EmailMultiAlternatives

from django.http import JsonResponse


# def send_message(name, email, phone):
#     text = get_template('message.html')
#     html = get_template('message.html')
#     context = {'name': name, 'email': email, 'phone': phone}
#     subject = 'Сообщение с сайта investsud'
#     from_email = 'info@investsud.ru'
#     text_content = text.render(context)
#     html_content = html.render(context)
#
#     msg = EmailMultiAlternatives(subject, text_content, from_email, ['info@investsud.ru'])
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()


class MessageForm(View):
    def post(self, request):
        if request.POST.get('action') == 'feedback_view':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            #form = FeedBackForm(request.POST)
            # if form.is_valid():
            #     print(form.cleaned_data)

            message = "\n" f"Имя: {name}" \
                      "\n" f"Телефон: {phone}" \
                      "\n" f"E-mail: {email}" \
            #           "\n" f"ИНН должника: {form.cleaned_data['inn']}" \
            #           "\n" f"Наименование должника: {form.cleaned_data['name_debt']}" \
            #           "\n" f"Получено судебное решение?: {form.cleaned_data['sud']}" \
            #           "\n" f"Сумма долга, руб: {form.cleaned_data['sum_debt']}" \
            #           "\n" f"Получен исполнительный лист?: {form.cleaned_data['list']}"
            mail = send_mail(name, message, 'info@investsud.ru',
                             ['sergeimakarenko5991@gmail.com'], fail_silently=False)
            print(name)
            if mail:
                print('success_message')
                FeedBackMoney.objects.create(
                    name=name,
                    phone=phone,
                    email=email
                )

                return JsonResponse({"name": name}, status=200)
            else:
                return JsonResponse({"phone": phone}, status=400)
        # else:
        #     form = FeedBackForm()



# class MessageLite(View):
#     def post(self, request):
#         if request.method == 'POST':
#             form = FeedBackLite(request.POST)
#             if form.is_valid():
#                 message = "\n" f"Имя: {form.cleaned_data['name']}" \
#                           "\n" f"Телефон: {form.cleaned_data['phone']}" \
#                           "\n" f"E-mail: {form.cleaned_data['email']}"
#                 mail = send_mail(form.cleaned_data['name'], message, 'info@investsud.ru',
#                                  ['sergeimakarenko5991@gmail.com'], fail_silently=False)
#                 if mail:
#                     print('success_message')
#                     form.save()
#                     return redirect('forms_success')
#                 else:
#                     print('error_message')
#         else:
#             form = FeedBackLite()
#
#
#
#
# def forms_success(request):
#     return render(request, 'forms/feedback_success.html')

