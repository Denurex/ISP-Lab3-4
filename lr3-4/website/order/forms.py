from django import forms
from django.forms import TextInput
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'city']
        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'style': 'width:250px; margin-top:50px'


            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'style': 'width:250px; margin-top:10px'
            }),
            "address": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес',
                'style': 'width:250px; margin-top:10px'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Город',
                'style': 'width:250px; margin-top:10px'
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for item in self.fields:
            self.fields[item].label = ''