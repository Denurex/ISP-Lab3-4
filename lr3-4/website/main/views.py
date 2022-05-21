"""Aplication logic"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def index(request):

    return render(request, 'main/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/info.html')


