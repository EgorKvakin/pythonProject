from django.contrib import admin
from .models import Film, Actor, Categories

# Register your models here.
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Categories)