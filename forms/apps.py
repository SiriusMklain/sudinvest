from django.apps import AppConfig


class FormsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forms'
    verbose_name = u'Формы с сайта'
    default_app_config = 'main.apps.MainConfig'