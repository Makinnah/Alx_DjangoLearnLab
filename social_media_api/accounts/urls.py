from django.urls import path
from .views import RegisterView, CustomObtainAuthToken, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='api_token_auth'),  # POST username & password -> token
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
# Task Two
from django.urls import path
from .views import follow_user, unfollow_user, following_list

urlpatterns = [
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
    path('following/', following_list, name='my-following'),
    path('following/<int:user_id>/', following_list, name='user-following'),
]

