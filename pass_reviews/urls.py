
from django.urls import path
from .views import PasswordResetView

urlpatterns = [
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    # Другие URL-маршруты вашего приложения
]
