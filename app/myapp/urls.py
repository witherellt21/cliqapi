from django.urls import path
from .views import *

urlpatterns = [
    path("", create_account, name="user-create"),
    path("login", login, name="login"),
]
