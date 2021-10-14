from abc import ABC, abstractclassmethod

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Game
from .serializers import GameSerializer


class Main(ABC):
    """
    Абстрактные классы широко фигурируют в ООП, часто всплывают в шаблонах
    проектирования. Они говорят, что общий интерфейс уже обозначен, но
    этот класс еще не предназначен для использования,
    кроме как для наследования от него конкретных потомков.

    Абстрактный класс не может быть инстанциирован (создан его экземпляр).
    Нужно наследовать этот класс и реализовать
    (переопределить) все абстрактные методы, и только после этого
    можно создавать экземпляры такого наследника.
    """

    @abstractclassmethod
    def check_email(self):
        pass


class Esp(Main):
    """
    Класс для проверки почты в ESP.
    """

    @abstractclassmethod
    def check_email(self, email):
        esp_db = ["pochta@mail.ru"]  # Абстрактная БД в ESP
        if email not in esp_db:  # Если почты нет в ESP
            esp_db.append(email)  # Добавляем почту в ESP
            return False
        else:
            return True


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

                title = Game.objects.get(email=request.data["email"])
                title.number_of_games += 1  # Если в базе игры почта есть, инкрементим в базе кол-во игр
                title.save()
                return JsonResponse(
                    {
                        "db_existed": True,
                        "number_of_games": title.number_of_games,
                    }
                )
            except:
                return JsonResponse(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return JsonResponse({"message": "An error has occurred"})
