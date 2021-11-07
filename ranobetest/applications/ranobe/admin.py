from django.contrib import admin

from applications.ranobe.models import Ranobe, Type, Tags, Genre

admin.site.register(Genre)
admin.site.register(Tags)
admin.site.register(Type)
admin.site.register(Ranobe)