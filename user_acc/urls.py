# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from django.urls import path
from .views import RegisterApi, test, LoginApi, LogoutApi, TokenRefresh


urlpatterns = [
    path('regis/', RegisterApi.as_view()),
    # path('login/', TokenObtainPairView.as_view()),
    path('login/', LoginApi.as_view()),

    path('token/refresh/', TokenRefresh.as_view()),
    # path('logout/', TokenBlacklistView.as_view()),
    path('logout/', LogoutApi.as_view()),
    path('test/', test),
]