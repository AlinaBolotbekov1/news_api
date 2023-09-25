from rest_framework.viewsets import ModelViewSet
from .serializers import VideoListSerializer, VideoDetailSerializer
from .models import Video
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from my_reviews.serializers import LikeSerializer
from my_reviews.models import Like
from rest_framework.response import Response
from rest_framework.decorators import action


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]

class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category','created_at']
    search_fields = ['title']


    def get_serializer_class(self):
        if self.action == 'list':
            return VideoListSerializer
        else:
            return self.serializer_class