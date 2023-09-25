# from django.urls import path, include  Алина эже вы может сюда url ки
from .views import CommentView, RatingView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('comments', CommentView)
router.register('ratings', RatingView)