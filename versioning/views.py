# 3rd party
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Application
from versioning.permissions import HasVersioningAPISecret
from versioning.serializers import CurrentWebAppVersionSerializer, WebAppVersionSerializer


class CurrentWebAppVersionView(APIView):
    permission_classes = [
        AllowAny,
    ]

    def get(self, request, format=None) -> Response:
        serializer = CurrentWebAppVersionSerializer({})
        return Response(serializer.data)


class WebAppVersionCreateView(CreateAPIView):
    serializer_class = WebAppVersionSerializer

    permission_classes = [
        HasVersioningAPISecret,
    ]
