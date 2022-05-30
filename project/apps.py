from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    verbose_name = u'Проекты'
    default_app_config = 'main.apps.MainConfig'
