from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, odj):
        return request.user.is_authenticated and odj.author == request.user