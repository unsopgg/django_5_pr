from rest_framework import generics


from applications.film.models import Film


from applications.film.serializer import FilmSerializer


class FilmListView(generics.ListAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
