from django.contrib import admin

from .models import *


class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'sum_debt')


class FormBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


admin.site.register(FeedBackMoney, FormAdmin)
admin.site.register(FeedBack, FormBackAdmin)