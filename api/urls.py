from django.urls import path

from .views import create_or_update_email

urlpatterns = [
    path("v1/emails/", create_or_update_email, name="emails"),
]
