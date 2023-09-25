from django.urls import path, include
from .views import VideoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('video', VideoView)



urlpatterns = [
    path('', include(router.urls)),
]