from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import user_views, movie_views

urlpatterns = [
    path('user/create/', user_views.create_user),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('movies/', movie_views.get_movies)
]
