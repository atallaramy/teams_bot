from django.urls import path
from .views import message

urlpatterns = [
    path("api/messages", message, name="message"),
]
