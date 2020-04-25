from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserCreate

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view()),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
