# Generated by Django 4.0.4 on 2022-04-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_investpost_investor_planned_annual_return_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investpost',
            name='planned_collection_period',
            field=models.FloatField(blank=True, null=True, verbose_name='Плановый срок взыскания'),
        ),
    ]
