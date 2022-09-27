from django.db import models

# Create your models here.
class Film(models.Model):
    film_title = models.CharField('Название фильма', max_length = 300)
    film_preview = models.ImageField('Превью фильма', upload_to = 'images/films')
    film_catergory = models.CharField('Категория фильма', max_length = 200)
    film_year = models.CharField('Дата выхода фильма', max_length = 50)
    film_type = models.CharField('Тип', max_length = 50)

    def __str__(self):
        return self.film_title

