from django import forms
from .models import FeedBackMoney


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
            'phone': forms.TextInput(attrs={'class': 'required', 'id': 'phone'}),
            'email': forms.TextInput(attrs={'class': 'required', 'id': 'email'}),
            'inn': forms.TextInput(attrs={'id': 'inn'}),
            'name_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'name_debt'}),
            'sud': forms.Select(),
            'sum_debt': forms.TextInput(attrs={'class': 'form-group', 'id': 'sum_debt'}),
            'list': forms.Select(),
        }
