from django.urls import path
from user.views import CustomTokenObtainPairView, UserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # 기본 jwt access 토큰 발급 view
    TokenRefreshView,  # jwt refresh 토큰 발급 view
)

urlpatterns = [
    path('register/', UserView.as_view()), # 회원가입
    path('login/', CustomTokenObtainPairView.as_view()),  # 로그인 url
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 시간마다 토큰 재발급
]