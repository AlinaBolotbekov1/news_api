from django.urls import path, include
from .views import NewsView, CategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryView)
router.register('news', NewsView)


urlpatterns = [
    path('', include(router.urls)),
]

