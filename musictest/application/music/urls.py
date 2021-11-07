from django.urls import path

from application.music.views import SongsListView

urlpatterns = [
    path('songs-list/', SongsListView.as_view()),
]