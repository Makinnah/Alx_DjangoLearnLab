from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),  # POST username & password -> token
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
