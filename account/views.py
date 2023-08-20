from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from .forms import RegistrationForm
from .models import Profile


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


class ProfileList(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = "profiles"

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    fields = [
        "name",
        "age_limit",
    ]
    initial = {
        "age_limit": "kids",
    }

    def get_success_url(self):
        return reverse("profile-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProfileCreate, self).form_valid(form)
