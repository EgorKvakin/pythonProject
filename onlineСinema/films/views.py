from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from datetime import datetime
from .models import Film,Actor


# Create your views here.

class FilmView(ListView):
    model = Film
    template_name = 'main.html'


def movieView(request, pk):
    try:
        film = Film.objects.get(id=pk)
    except:
        raise Http404("Фильм не найден!")
    categories = getattr(film, 'film_catergory').split(',')
    actors = Actor.objects.filter(actor_film_list = pk)
    return render(request, 'Films/film_view.html', {'film': film , 'categories': categories , 'actors': actors})

def actorCard(request,pk):
    try:
        actor = Actor.objects.get(pk=pk)
    except:
        raise Http404("Актер не найден")
    films = Film.objects.filter(film_title = actor.actor_film_list)
    today = datetime.today()
    year = today.year - actor.birthday.year
    return render(request, 'Films/actor_card.html', {'actor':actor , 'films':films , 'year':year})