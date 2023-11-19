from django.urls import path
from .views import index, contacts, help

urlpatterns = [
    path("", index, name="index"),
    path("contacts/", contacts, name="contacts"),
    path("help/", help, name="help"),
]
