from django.urls import path

from . import views

urlpatterns = [
    path("wiki/<str:title>", views.entry, name="entry"),
    path("", views.index, name="index"),
     
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random_title", views.random_title, name="random_title"),
]
