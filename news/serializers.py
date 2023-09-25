from rest_framework.serializers import ModelSerializer
from .models import Category, News
from django.db.models import Avg
from my_reviews.serializers import CommentSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['title', 'category', 'slug']



class NewsDetailSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        rep['likes'] = instance.likes.all().count()
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return rep



    
    