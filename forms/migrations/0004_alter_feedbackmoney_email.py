# Generated by Django 3.2.6 on 2022-04-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20220417_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmoney',
            name='email',
            field=models.CharField(blank=True, max_length=120, verbose_name='Email'),
        ),
    ]
