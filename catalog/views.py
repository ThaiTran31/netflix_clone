from django.shortcuts import render
from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("profile-list")
    return render(request, "index.html")
