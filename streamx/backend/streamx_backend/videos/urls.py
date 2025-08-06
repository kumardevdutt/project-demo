from django.urls import path
from .views import RegisterView, VideoListView, VideoUploadView, UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]
