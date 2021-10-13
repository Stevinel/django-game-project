from django.contrib import admin

from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "number_of_games")
    search_fields = ("email",)
    list_filter = ("number_of_games",)
    empty_value_display = "-пусто-"
