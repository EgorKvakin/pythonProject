from django.urls import path

from . import views

urlpatterns = [
    path('', views.FilmView.as_view(), name='main'),
    path('film/<int:pk>/', views.MovieView, name = 'movie_view'),
]