from rest_framework import serializers

from .models import Game


class GameSerializer(serializers.ModelSerializer):
    """Сериалайзер данных об игре"""

    class Meta:
        model = Game
        fields = ["email", "number_of_games"]
