# posts/urls.py
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
#Task Two
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    # ... other post routes
]


#Task Three
from django.urls import path
from . import views

urlpatterns = [
    # existing post endpoints ...
    path('posts/<int:pk>/like/', views.like_post, name='post-like'),
    path('posts/<int:pk>/unlike/', views.unlike_post, name='post-unlike'),
]

