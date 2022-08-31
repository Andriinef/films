from django.urls import path

from .views import *


urlpatterns = [  # список шаблонов, определяющий маршрутизацию
    path("", MoviesView.as_view(), name="movies"),
]
