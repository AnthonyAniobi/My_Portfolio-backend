from unicodedata import category
from django.db import models
from . import category

class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title of Work')
    sub_title = models.CharField(max_length=250, verbose_name='Subtitle of Work')
    first_category = models.ManyToManyField(category.Category)
    image_url = models.URLField(verbose_name='url of image')
    alt_text = models.CharField(max_length=250, verbose_name='alternative image text')
    store_url = models.URLField(null=True, verbose_name='url of live view')
    