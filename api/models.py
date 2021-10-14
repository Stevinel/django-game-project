from django.db import models


class Game(models.Model):
    """
    Модель электронного адреса
    """

    email = models.EmailField("Электронный адрес", max_length=50, unique=True)
    number_of_games = models.PositiveBigIntegerField(
        "Количество игр", null=True
    )

    class Meta:
        verbose_name = "Электронный адрес"
        verbose_name_plural = "Электронные адреса"

    def __str__(self):
        return self.email
