from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class CustomObtainAuthToken(ObtainAuthToken):
    """
    Returns token and basic user info when posting username & password.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = token.user
        return Response({'token': token.key, 'user_id': user.id, 'username': user.username})

class UserDetailView(generics.RetrieveAPIView):
    """
    Retrieve a user's public profile (by pk).
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# follow feed
# accounts/views.py
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .serializers import UserSimpleSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    me = request.user
    target = get_object_or_404(User, pk=user_id)
    if me == target:
        return Response({"detail": "Cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    me.follow(target)
    return Response(UserSimpleSerializer(target).data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    me = request.user
    target = get_object_or_404(User, pk=user_id)
    me.unfollow(target)
    return Response({"detail": "Unfollowed"}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def following_list(request, user_id=None):
    # Get following list for specified user or current user
    if user_id:
        user = get_object_or_404(User, pk=user_id)
    else:
        user = request.user
    qs = user.following.all()
    return Response(UserSimpleSerializer(qs, many=True).data)

