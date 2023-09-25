from .views import CommentView, RatingView, FavoriteView
from rest_framework.routers import DefaultRouter
from django.urls import path, include




router = DefaultRouter()
router.register('comments', CommentView)
router.register('ratings', RatingView)
router.register('favorites', FavoriteView)

urlpatterns = [
    path('', include(router.urls)),
]
