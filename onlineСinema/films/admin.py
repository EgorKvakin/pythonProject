from django.contrib import admin
from .models import Film, Actor, Categories, Series, SeriesVideo

# Register your models here.
class SeriesVideoAdmin(admin.ModelAdmin):
  pass
class SeriesVideoInline(admin.StackedInline):
  model = SeriesVideo


class SeriesVideoAdmin(admin.ModelAdmin):
  inlines = [SeriesVideoInline,]

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Categories)
admin.site.register(Series,SeriesVideoAdmin)