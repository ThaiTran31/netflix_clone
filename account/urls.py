from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="account/login.html",
            redirect_authenticated_user=True
        ),
        name="log-in"
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page="/"
        ),
        name="log-out"
    ),
    path("signup/", views.register_view, name="sign-up"),
]
