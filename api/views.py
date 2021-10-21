from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Game
from .serializers import GameSerializer
from .services import Esp, Main


class MyDB(Main):
    """
    Класс для проверки почты в БД игры.
    """

    @api_view(["POST"])
    def check_email(request):
        """
        Функция создаёт или обновляет электронную почту в БД,
        а так же прибавляет кол-во игр в зависимости от условий.
        """
        if request.method == "POST":
            try:
                serializer = GameSerializer(data=request.data)

                if serializer.is_valid():  # Если в базе игры почты нет
                    Game.objects.create(
                        email=request.data["email"], number_of_games="1"
                    )  # Бэкенд записывает в свою базу факт игры
                    esp_results = Esp.check_email(
                        request.data["email"]
                    )  # Возвращает информацию о существовании почты в БД
                    return JsonResponse(
                        {
                            "db_existed": False,
                            "esp_existed": esp_results,
                            "number_of_games": 1,
                        }
                    )

                game = Game.objects.get(email=request.data["email"])
                game.number_of_games += 1  # Если в базе игры почта есть, инкрементим в базе кол-во игр
                game.save()
                return JsonResponse(
                    {
                        "db_existed": True,
                        "number_of_games": game.number_of_games,
                    }
                )
            except:
                return JsonResponse(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse({"message": "An error has occurred"})
