from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import RegistrationForm


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
            return redirect("/")
    else:
        if request.user.is_authenticated:
            return redirect("/")
        form = RegistrationForm()
    context = {
        "form": form,
    }
    return render(request, "account/signup.html", context=context)
