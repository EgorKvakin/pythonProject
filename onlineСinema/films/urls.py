from django.urls import path

from . import views

urlpatterns = [
    path('', views.FilmView.as_view(), name='main'),
    path('film/<int:pk>/', views.movieView, name = 'movie_view'),
    path('actor/<int:pk>/', views.actorCard, name = 'actor_card'),
    path('category/<int:pk>/', views.categoryFilmsView, name = 'category'),
    path(r'^ajax/autocomplete/$', views.autocomplete, name='ajax_autocomplete'),
]