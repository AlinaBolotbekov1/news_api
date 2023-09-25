from rest_framework.serializers import ModelSerializer
from .models import Video
from my_reviews.serializers import CommentSerializer
from django.db.models import Avg

class VideoListSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['video', 'title', 'category']


class VideoDetailSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
