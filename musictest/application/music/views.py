from rest_framework import generics

from application.music.models import Music

from application.music.serializers import MusicSerializer


class SongsListView(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
