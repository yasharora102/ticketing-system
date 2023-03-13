from django.urls import path, include

# import render

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    # path("search/", views.get_anime_from_JIKAN, name="search"),
    # path("sample/", views.sample_data_insertion, name="sample")
]
