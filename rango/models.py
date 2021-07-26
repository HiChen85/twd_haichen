from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name="category", max_length=128, unique=True)
    views = models.IntegerField(verbose_name='views', default=0)
    likes = models.IntegerField(verbose_name='likes', default=0)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Categories'


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="title", max_length=128)
    url = models.URLField()
    views = models.IntegerField(verbose_name="views", default=0)

    def __str__(self):
        return self.title