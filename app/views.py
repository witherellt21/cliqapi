from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def getHealth(request):
    return Response(data={"health": "UP"}, content_type="application/json")
