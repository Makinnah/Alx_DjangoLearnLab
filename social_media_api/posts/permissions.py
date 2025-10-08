# posts/permissions.py
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allow read-only for any request; write permissions only to the object's author.
    """
    def has_permission(self, request, view):
        # Allow any user to list/retrieve; creation requires authentication
        if view.action in ['list', 'retrieve']:
            return True
        if view.action == 'create':
            return request.user and request.user.is_authenticated
        # other actions deferr to has_object_permission
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # SAFE methods allowed for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # write permissions only for the author
        return obj.author == request.user
