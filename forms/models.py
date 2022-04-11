from django.db import models


class FeedBackMoney(models.Model):
    """Форма обратной связи на продажу долга"""
    status_list = (
        ('yes', 'Да'),
        ('no', 'Нет')
    )
    sud_list = (
        ('yes', 'Да'),
        ('no', 'Нет')
    )
    name = models.CharField(max_length=120, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(max_length=120, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон', null=True, blank=True)
    inn = models.CharField(max_length=50, verbose_name='ИНН должника', null=True, blank=True)
    name_debt = models.CharField(max_length=50, verbose_name="Наименование должника", null=True, blank=True)
    sud = models.CharField(max_length=50, verbose_name="Получено судебное решение?", choices=sud_list, null=True, blank=True)
    sum_debt = models.CharField(max_length=50, verbose_name="Сумма долга, руб", null=True, blank=True)
    list = models.CharField(max_length=50, verbose_name="Получен исполнительный лист?", choices=status_list, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка на продажу долга'
        verbose_name_plural = 'Заявки на продажу долгов'


class FeedBack(models.Model):
    """Форма обратной связи"""
    name = models.CharField(max_length=120, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(max_length=120, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=15, verbose_name='Телефон', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка с сайта'
        verbose_name_plural = 'Заявки с сайта'

