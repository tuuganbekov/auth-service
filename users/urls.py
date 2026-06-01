from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from .views import RegisterAPIView, TestAPIView


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterAPIView.as_view()),
    path("test/", TestAPIView.as_view()),
]
