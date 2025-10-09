# posts/views.py
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for Posts.
    """
    queryset = Post.objects.all().select_related('author').prefetch_related('comments')
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author__username', 'created_at']  # fields available for exact/enum filtering
    search_fields = ['title', 'content', 'author__username']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']  # default ordering

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for comments. Only comment authors may update/delete.
    """
    queryset = Comment.objects.all().select_related('author', 'post')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['post', 'author__username', 'created_at']
    search_fields = ['content', 'author__username']
    ordering_fields = ['created_at']
    ordering = ['created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

#Task 2
# posts/views.py
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()  # assuming `following` is on CustomUser
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

#Task Three
# posts/views.py (append)
# posts/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if Like.objects.filter(user=user, post=post).exists():
        return Response({"message": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
    Like.objects.create(user=user, post=post)
    if post.author != user:
        Notification.objects.create(recipient=post.author, actor=user, verb="liked your post", target=post)
    return Response({"message": "Liked"}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    like = Like.objects.filter(user=user, post=post).first()
    if not like:
        return Response({"message": "Not liked yet"}, status=status.HTTP_400_BAD_REQUEST)
    like.delete()
    return Response({"message": "Unliked"}, status=status.HTTP_200_OK)

