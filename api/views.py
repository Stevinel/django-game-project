from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer


@api_view(["POST"])
def create_or_update_email(request):
    """
    Функция создаёт или обновляет электронную почту в БД,
    а так же прибавляет кол-во игр в зависимости от условий.
    """
    if request.method == "POST":
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():  # Если почта ещё не существует
            Game.objects.create(
                email=request.data["email"], number_of_games="1"
            )  # Создаём почту
            return Response(
                {"message": "Почта добавлена", "number_of_games": "1"}
            )
        title = Game.objects.get(email=request.data["email"])
        title.number_of_games += (
            1  # Если почта существует, инкрементим в базе кол-во игр
        )
        title.save()
        return Response(
            {
                "message": "Почта уже существует",
                "number_of_games": title.number_of_games,
            }
        )
    return Response({"message": "Неверный запрос"})
