from django import forms
from .models import FilmComments, SeriesComments

class FilmCommentForm(forms.ModelForm):
    class Meta:
        model = FilmComments
        fields = ('comment',)

class SeriesCommentForm(forms.ModelForm):
    class Meta:
        model = SeriesComments
        fields = ('comment',)
