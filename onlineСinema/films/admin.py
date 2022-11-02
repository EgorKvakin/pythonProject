from django.contrib import admin
from .models import Film, Actor, Categories, Series, SeriesVideo, Seasons
import nested_admin

# Register your models here.
class SeriesVideoInlines(nested_admin.NestedStackedInline):
    model = SeriesVideo

class SeasonsInlines(nested_admin.NestedStackedInline):
    model = Seasons
    inlines = [SeriesVideoInlines,]

class SeasonsAdmin(nested_admin.NestedModelAdmin):
    inlines = [SeasonsInlines,]

class SeriesVideoAdmin(admin.ModelAdmin):
    inlines = [SeriesVideoInlines,]

admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Categories)
admin.site.register(Series,SeasonsAdmin)