from rest_framework.generics import CreateAPIView
from rest_framework import views, response, status
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer


class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterSerializer


class TestAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return response.Response(
            {
                "msg": "ok"
            },
            status=status.HTTP_200_OK
        )