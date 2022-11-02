from datetime import datetime

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Film(models.Model):
    film_title = models.CharField('Название фильма', max_length = 300)
    film_preview = models.ImageField('Превью фильма', upload_to = 'images/films')
    film_year = models.CharField('Дата выхода фильма', max_length = 50)
    description = models.TextField()
    film_file = models.FileField(upload_to = 'video/' , validators = [FileExtensionValidator(allowed_extensions = ['mp4'])])
    actor_film_list = models.ManyToManyField('Actor')
    film_list = models.ManyToManyField('Categories')

    def __str__(self):
        return self.film_title

class Series(models.Model):
    series_title = models.CharField('Название сериала', max_length = 300)
    series_preview = models.ImageField('Превью сериала', upload_to = 'images/films')
    series_year = models.CharField('Дата выхода сериала', max_length = 50)
    description = models.TextField()
    series_count = models.PositiveBigIntegerField('Кол-во серий')
    seasons_count = models.PositiveIntegerField('Кол-во сезонов')
    actor_film_list = models.ManyToManyField('Actor')
    film_list = models.ManyToManyField('Categories')

    def __str__(self):
        return self.series_title
class SeriesVideo(models.Model):
    series_index = models.IntegerField('Номер серии',default=0)
    series_file = models.FileField(upload_to = 'video/series/%Y/%m/%d' , validators = [FileExtensionValidator(allowed_extensions = ['mp4'])])
    series_ind = models.ForeignKey('Series',on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField('Имя',max_length = 300)
    surname = models.CharField('Фамилия',max_length = 300)
    actor_photo = models.ImageField('Фото актера',upload_to = 'images/actors')

    birthday = models.DateField('День рожденья',null=True)
    def __str__(self):
        return self.name

class Categories(models.Model):
    category = models.CharField('Название',max_length = 300)

    def __str__(self):
        return self.category