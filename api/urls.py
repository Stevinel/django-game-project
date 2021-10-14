from django.urls import path

from .views import MyDB

urlpatterns = [
    path("v1/emails/", MyDB.check_email, name="emails"),
]
