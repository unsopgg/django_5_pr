from django.contrib import admin


from applications.film.models import Film, Studio, Genre


admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Film)
