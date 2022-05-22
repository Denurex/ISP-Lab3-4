from .models import Comment
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationn(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "comment"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control input-text',
                'placeholder': 'Имя'

        }),
            "comment": Textarea(attrs={
                'class': 'form-control input-text text-area',
                'placeholder': 'Сообщение',
                'rows': 5
            }),
        }