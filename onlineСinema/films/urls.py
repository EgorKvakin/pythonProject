from django.urls import path

from . import views

urlpatterns = [
    path('', views.FilmView.as_view(), name='main'),
    path('film/<int:pk>/', views.movieView, name = 'movie_view'),
    path('series/<int:pk>/', views.seriesView, name = 'series_view'),
    path('actor/<int:pk>/', views.actorCard, name = 'actor_card'),
    path('category/<int:pk>/', views.categoryFilmsView, name = 'category'),
    path('autocomplete/', views.autocompleteModel , name = 'autocomplete' ),
    path('search/', views.Search.as_view(), name ='search' ),
]