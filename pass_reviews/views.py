# views.py
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .serializers import PasswordResetSerializer

class PasswordResetView(generics.CreateAPIView):
    serializer_class = PasswordResetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'detail': 'Пользователь с таким email не найден.'}, status=400)
        
        # Генерируем и отправляем ссылку для сброса пароля по электронной почте
        # Здесь вы можете использовать библиотеку для генерации токенов, например, Django Rest Framework Token или JWT
        # и отправить ссылку с токеном на указанный email
        # Пример отправки ссылки:
        reset_url = f'{settings.FRONTEND_URL}/reset-password?token={token}'
        send_mail(
            'Сброс пароля',
            f'Для сброса пароля перейдите по ссылке: {reset_url}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        
        return Response({'detail': 'Ссылка для сброса пароля отправлена на ваш email.'}, status=200)
