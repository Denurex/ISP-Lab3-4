from django.shortcuts import redirect, render

from .forms import UserRegistration


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page")
    else:
        form = UserRegistration()
    return render(request, "authorization/sign_up.html", {"form": form})
