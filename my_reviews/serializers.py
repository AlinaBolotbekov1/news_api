from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from .models import Like, Comment, Rating, Favorite
from news import serializers as NewsListSerializer



class CommentSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = '__all__'


    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(author=user, **validated_data)
        return comment


class RatingSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if rating in range(1, 11):
            return rating
        raise ValidationError(
            'Рейтинг должен быть от 1 до 10'
        )

    def validate_news(self, news):
        user = self.context.get('request').user
        if self.Meta.model.objects.filter(news=news, author=user).exists():
            raise ValidationError(
                'Вы уже оставляли отзыв на данную новость'
            )
        return news
    
    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)


class LikeSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')
    news = ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)



class FavoriteListSerializer(ModelSerializer):
    news = NewsListSerializer
    

    class Meta:
        model = Favorite
        fields = ['news']
       


class FavoriteDetailSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Favorite
        fields = '__all__'


    def create(self, validated_data):
        user = self.context.get('request').user
        return self.Meta.model.objects.create(author=user, **validated_data)
