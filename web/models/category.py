from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Name of Category')
    description= models.TextField(default='no description', verbose_name='Description of Category')