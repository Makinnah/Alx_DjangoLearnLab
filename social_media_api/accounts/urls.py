from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),  # POST username & password -> token
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
# Task Two
from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_id>/', views.FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', views.UnfollowUserView.as_view(), name='unfollow-user'),
]

