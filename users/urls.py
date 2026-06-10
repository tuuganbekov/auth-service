from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


from .views import RegisterAPIView, CustomTokenObtainPairView, TestAPIView


urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", RegisterAPIView.as_view()),
    path("test/", TestAPIView.as_view()),
]
