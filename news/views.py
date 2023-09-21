from .models import Category, News
from .serializers import CategorySerializer, NewsDetailSerializer, NewsListSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from bs4 import BeautifulSoup
import requests

class PermissionMixin:
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy', 'create'):
            permissions = [IsAuthenticated]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]
    

class CategoryView(PermissionMixin,ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsView(PermissionMixin,ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category','created_at']
    search_fields = ['title']



    def get_serializer_class(self):
        if self.action == 'list':
            return NewsListSerializer
        else:
            return self.serializer_class
    
