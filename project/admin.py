from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('projectNumber', 'date_pub', 'statusProject')


admin.site.register(InvestPost, PostAdmin)
