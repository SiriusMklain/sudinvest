from django import forms
from .models import *


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBackMoney
        status_choice = (
            ('Да', 'yes'),
            ('Нет', 'no')
        )
        sud_choice = (
            ('Да', 'yes'),
            ('Нет', 'no')
        )
        fields = ['name', 'phone', 'email', 'inn', 'name_debt', 'sud', 'sum_debt', 'list']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'required', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'required', 'id': 'phone', 'type': 'tel'}),
            'email': forms.TextInput(attrs={'class': 'required email', 'id': 'email'}),
            'inn': forms.TextInput(attrs={'id': 'inn', 'class': 'inn'}),
            'name_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'name_debt'}),
            'sud': forms.Select(),
            'sum_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'sum_debt'}),
            'list': forms.Select(),
        }


class FeedBackLite(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'phone', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'required', 'id': 'name'}),
            'phone': forms.TextInput(attrs={'class': 'required', 'id': 'phone', 'type': 'tel'}),
            'email': forms.TextInput(attrs={'class': 'required', 'id': 'email'}),
        }
