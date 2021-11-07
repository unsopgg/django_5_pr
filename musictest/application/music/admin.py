from django.contrib import admin

from application.music.models import Category, Music

admin.site.register(Category)
admin.site.register(Music)