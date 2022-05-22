"""Aplication logic"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Comment, Product
from .forms import CommentForm, UserRegistrationn


def index(request):
    tasks = Comment.objects.all()
    return render(request, 'main/base.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
        else:
            error = 'GG'


def check_product(request):
    product = Product.objects.all()
    return render(request, 'main/product.html')


def shop(request):
    product = Product.objects.all()
    context = {
        'pr': product
    }
    return render(request, 'main/product.html', context)


def shop_cart(request):

    return render(request, 'main/shopping_cart.html')
