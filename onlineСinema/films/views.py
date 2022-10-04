from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View
from .models import Film


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
    return render(request, 'Films/film_view.html', {'film': film , 'categories': categories})
