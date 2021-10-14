from abc import ABC, abstractclassmethod


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
