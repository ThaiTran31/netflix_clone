from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Video
from account.models import Profile


def home(request):
    if request.user.is_authenticated:
        return redirect("profile-list")
    return render(request, "index.html")


class MovieList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = "movies"

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def get_queryset(self):
        profile = get_object_or_404(Profile, id=self.kwargs["profile_id"])
        maturity_level = self.request.session.get("maturity_level", profile.age_limit)
        self.request.session["maturity_level"] = maturity_level
        return Movie.objects.filter(age_limit__exact=maturity_level)

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        if context["movies"]:
            context["show_case"] = context["movies"][0]
        return context


class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie


class VideoShow(LoginRequiredMixin, DetailView):
    model = Video
