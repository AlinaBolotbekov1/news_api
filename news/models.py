from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Наименование категории',
                             unique=True)
    slug = models.SlugField(primary_key=True,
                            blank=True,
                            max_length=20)
    
    def __str__(self):
        return self.title
    

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()



class News(models.Model):
    title = models.CharField(max_length=200,
                             unique=True,
                             verbose_name='Заголовок')
    category = models.ForeignKey(Category, 
                                 related_name='news',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    slug = models.SlugField(primary_key=True,
                            blank=True,
                            max_length=200)
    image = models.ImageField(upload_to='images/', 
                            verbose_name='Картинка')
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
