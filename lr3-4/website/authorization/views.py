from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistration
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST);
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('main_page')
    else:
        form = UserRegistration()
    return render(request, 'authorization/sign_up.html', {'form': form})
