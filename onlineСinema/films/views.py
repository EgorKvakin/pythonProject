from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, ListView, View
from datetime import datetime
from django.template import RequestContext
from .models import Film, Actor, Categories


# Create your views here.

class FilmView(ListView):
    model = Film
    template_name = 'main.html'

def movieView(request, pk):
    try:
        film = Film.objects.get(id=pk)
    except:
        raise Http404("Фильм не найден!")
    # categories = getattr(film, 'film_catergory').split(',')
    categories = Film.objects.get(pk=pk).film_list.all()
    actors = Film.objects.get(pk=pk).actor_film_list.all()
    return render(request, 'Films/film_view.html', {'film': film, 'categories': categories, 'actors': actors})


def actorCard(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except:
        raise Http404("Актер не найден")
    films = Film.objects.filter(actor_film_list=pk)
    today = datetime.today()
    year = today.year - actor.birthday.year
    return render(request, 'Films/actor_card.html', {'actor': actor, 'films': films, 'year': year})


def categoryFilmsView(request, pk):
    try:
        categories = Categories.objects.get(pk=pk)
    except:
        raise Http404("Категория не найдена")
    films = Film.objects.filter(film_list=pk)
    return render(request, 'Films/category_list.html', {'categories': categories, 'films': films})
