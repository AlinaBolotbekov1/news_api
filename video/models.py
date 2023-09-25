from django.db import models
from news.models import Category

class Video(models.Model):
    video = models.FileField(
        upload_to='video_news/',
        verbose_name='Видео')
    category = models.ForeignKey(
        Category,
        related_name='videos',
        on_delete=models.CASCADE,
        verbose_name='Категория')
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Заголовок')
    created_at = models.DateTimeField(auto_now_add=True)
    # views_qty  = models.PositiveIntegerField(default=0)
    description = models.TextField()


    def __str__(self):
        return f'{self.video} - {self.created_at}'


