from rest_framework import generics


from applications.game.models import Game


from applications.game.serializer import GameSerializer


class GameListView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
