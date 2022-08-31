from django.shortcuts import render
from django.views.generic import ListView

from .models import Movie


# Create your views here.
class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "КИНОАФИША"
        return context
