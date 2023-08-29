from django.urls import path
from .views import *


urlpatterns = [
    path("", UserCreateAPIView.as_view(), name="user-create"),
]
