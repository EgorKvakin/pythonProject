from django.urls import path

from . import views

urlpatterns = [
    path('', views.filmView, name='main'),
    path('get_data_films/',views.getDataFilms, name='get_data_films'),
    path('get_data_series/',views.getDataSeries, name='get_data_series'),
    path('film/<int:pk>/', views.movieView, name = 'movie_view'),
    path('series/<int:pk>/', views.seriesView, name = 'series_view'),
    path('actor/<int:pk>/', views.actorCard, name = 'actor_card'),
    path('films/category/<int:pk>/', views.categoryFilmsView, name = 'category_films'),
    path('series/category/<int:pk>/', views.categorySeriesView, name = 'category_series'),
    path('cartoon/category/<int:pk>/', views.categoryCartoonView, name = 'category_cartoon'),
    path('autocomplete/', views.autocompleteModel , name = 'autocomplete' ),
    path('getseason/<int:pk>/<int:season_ind>',views.getSeason, name = 'getseason'),
    path('getepisode/<int:pk>/<int:episode_ind>/<int:season_ind>',views.getEpisode, name = 'getepisode'),
    path('filmreview/<int:film_pk>/<int:author_pk>', views.FilmAddRewiew.as_view(), name='add_film_review'),
    path('seriesreview/<int:series_pk>/<int:author_pk>', views.SeriesAddRewiew.as_view(), name='add_series_review'),
]