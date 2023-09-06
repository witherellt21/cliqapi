from django.urls import reverse, resolve
from rest_framework.test import APIRequestFactory
from rest_framework import status


def test_get_configurations_view():
    url = reverse("options-configuration")
    view = resolve(url).func

    request = APIRequestFactory().get(reverse("options-configuration"))
    response = view(request)
    assert response.status_code == status.HTTP_200_OK
