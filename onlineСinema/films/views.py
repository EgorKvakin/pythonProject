from django.http import Http404, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, HttpResponse , redirect
from django.views.generic import TemplateView, ListView, View
from datetime import datetime
from django.core.paginator import Paginator
from django.template import RequestContext
from django.http import JsonResponse
from .models import Film, Actor, Categories, Series, SeriesVideo, Seasons, SeriesComments, FilmComments
from .forms import FilmCommentForm, SeriesCommentForm
from users.models import CustomUser
# Create your views here.
# Главная

def filmView(request):
    return render(request,'index.html')

def getDataFilms(request):
    films = list(Film.objects.values())
    series = list(Series.objects.values())
    return JsonResponse(films,safe=False)

def getDataSeries(request):
    series = list(Series.objects.values())
    return JsonResponse(series,safe=False)
# Фильмы
def movieView(request, pk):
    try:
        film = Film.objects.get(id=pk)
    except:
        raise Http404("Фильм не найден!")
    categories = Film.objects.get(pk=pk).film_list.all()
    actors = Film.objects.get(pk=pk).actor_film_list.all()
    comments = FilmComments.objects.filter(film = pk)
    return render(request, 'Films/film_view.html', {'film': film, 'categories': categories, 'actors': actors, 'comments':comments})


def actorCard(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except:
        raise Http404("Актер не найден")
    series = Series.objects.filter(actor_film_list=pk)
    films = Film.objects.filter(actor_film_list=pk)
    today = datetime.today()
    year = today.year - actor.birthday.year
    return render(request, 'Films/actor_card.html', {'actor': actor, 'films': films, 'year': year, 'series': series})


def categoryFilmsView(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except:
        raise Http404("Категория не найдена")
    films = Film.objects.filter(film_list=pk, tag = '1')
    paginator = Paginator(films,2)
    page_number = request.GET.get('page')
    films = paginator.get_page(page_number)
    return render(request, 'Films/category_list.html', {'categories': categories, 'page_obj': films})

# Поиск
def autocompleteModel(request):
    query_original = request.GET.get('search')
    if(query_original != ''):
        queryset_film = Film.objects.filter(film_title__icontains = query_original)
        queryset_series = Series.objects.filter(series_title__icontains=query_original)
    list = []
    for film in queryset_film:
        list.append({
            "name":film.film_title,
            "id":film.pk,
            "ind":'film'
        })
    for serie in queryset_series:
        list.append({
            "name":serie.series_title,
            "id":serie.pk,
            "ind":'series'
        })
    return JsonResponse({
        'status':True,
        'list':list
    })

# Сериалы

def seriesView(request, pk):
    try:
        series = Series.objects.get(id=pk)
    except:
        raise Http404("Сериал не найден!")
    categories = Series.objects.get(pk=pk).film_list.all()
    actors = Series.objects.get(pk=pk).actor_film_list.all()
    seasons = Seasons.objects.filter(season_ind=pk)
    season_first = Seasons.objects.filter(season_ind=pk).first()
    season_index = season_first.pk
    series_files = SeriesVideo.objects.filter(series_ind = season_index)
    episode_one = series_files.get(series_index = 1)
    comments = SeriesComments.objects.filter(series=pk)
    return render(request, 'Series/series_view.html', {'series': series, 'categories': categories, 'actors': actors, 'season_index':season_index, 'seasons':seasons, 'series_files':series_files, 'episode_one': episode_one, 'comments':comments})

def getSeason(request,pk,season_ind):
    try:
        series = Series.objects.get(id=pk)
    except:
        raise Http404("Сериал не найден!")
    categories = Series.objects.get(pk=pk).film_list.all()
    actors = Series.objects.get(pk=pk).actor_film_list.all()
    seasons = Seasons.objects.filter(season_ind=pk)
    series_files = SeriesVideo.objects.filter(series_ind=season_ind)
    season_index = season_ind
    comments = SeriesComments.objects.filter(series=pk)
    filter = series_files.get(series_index = 1)
    return render(request, 'Series/series_view.html',{'series': series, 'categories': categories, 'season_index':season_index, 'episode':filter, 'actors': actors, 'seasons':seasons, 'series_files':series_files, 'comments':comments})

def getEpisode(request,pk,episode_ind,season_ind):
    try:
        series = Series.objects.get(id=pk)
    except:
        raise Http404("Сериал не найден!")
    categories = Series.objects.get(pk=pk).film_list.all()
    actors = Series.objects.get(pk=pk).actor_film_list.all()
    seasons = Seasons.objects.filter(season_ind=pk)
    series_files = SeriesVideo.objects.filter(series_ind=season_ind)
    season_index = season_ind
    comments = SeriesComments.objects.filter(series=pk)
    filter = series_files.get(series_index = episode_ind)
    return render(request, 'Series/series_view.html',{'series': series, 'categories': categories, 'season_index':season_index, 'episode':filter, 'actors': actors, 'seasons':seasons, 'series_files':series_files, 'comments':comments})
def categorySeriesView(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except:
        raise Http404("Категория не найдена")
    series = Series.objects.filter(film_list=pk, tag = '1')
    paginator = Paginator(series,1)
    page_number = request.GET.get('page')
    series = paginator.get_page(page_number)
    return render(request, 'Series/category_series_list.html', {'categories': categories, 'page_obj': series})

# Мультфильмы

def categoryCartoonView(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except:
        raise Http404("Категория не найдена")
    series = Series.objects.filter(film_list=pk, tag='2')
    films = Film.objects.filter(film_list=pk, tag = '2')
    paginator_series = Paginator(series,1)
    paginator_films = Paginator(films,1)
    page_number = request.GET.get('page')
    series = paginator_series.get_page(page_number)
    films = paginator_films.get_page(page_number)
    return render(request, 'Cartoons/category_cartoons_list.html', {'categories': categories, 'series': series, 'page_obj': films})

# Комментарии

class FilmAddRewiew(View):
    def post(self, request, film_pk, author_pk):
        form = FilmCommentForm(request.POST)
        film = Film.objects.get(pk = film_pk)
        author = CustomUser.objects.get(pk = author_pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.film = film
            form.author = author
            form.save()
        url = f'/film/{film_pk}'
        return redirect(url)

class SeriesAddRewiew(View):
    def post(self, request, series_pk, author_pk):
        form = SeriesCommentForm(request.POST)
        series = Series.objects.get(pk = series_pk)
        author = CustomUser.objects.get(pk = author_pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.series = series
            form.author = author
            form.save()
        url = f'/series/{series_pk}'
        return redirect(url)