from django.urls import path

from applications.game.views import GameListView

urlpatterns = [
    path('game-list/', GameListView.as_view())
]