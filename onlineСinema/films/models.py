from datetime import datetime

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Film(models.Model):
    film_title = models.CharField('Название фильма', max_length = 300)
    film_preview = models.ImageField('Превью фильма', upload_to = 'images/films')
    film_catergory = models.CharField('Категория фильма', max_length = 200)
    film_year = models.CharField('Дата выхода фильма', max_length = 50)
    film_type = models.CharField('Тип', max_length = 50)
    description = models.TextField()
    film_file = models.FileField(upload_to = 'video/' , validators = [FileExtensionValidator(allowed_extensions = ['mp4'])])
    actor_film_list = models.ManyToManyField('Actor')
    film_list = models.ManyToManyField('Categories')

    def __str__(self):
        return self.film_title

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