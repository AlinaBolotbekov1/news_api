from .models import Comment, Rating, Favorite
from rest_framework.viewsets import ModelViewSet
from .serializers import CommentSerializer, RatingSerializer, FavoriteDetailSerializer, FavoriteListSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .peremissions import IsAuthorOrReadOnly


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]

        elif self.action in ('update', 'partial_update', 'destroy'):
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class RatingView(PermissionMixin, ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class FavoriteView(PermissionMixin, ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteListSerializer
        else:
            return self.serializer_class