from django.contrib import admin


from applications.game.models import Game, Platform, Genre


admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Game)
