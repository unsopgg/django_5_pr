from rest_framework import serializers


from applications.game.models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'