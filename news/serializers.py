from rest_framework.serializers import ModelSerializer
from .models import Category, News


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



    
    