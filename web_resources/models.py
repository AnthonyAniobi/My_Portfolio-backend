from django.db import models

class Categories(models.Model):
    '''model for categories'''
    title = models.CharField(max_length=100, verbose_name='store category')
    # add images to categories

class Product(models.Model):
    '''model for product'''
    title = models.CharField(max_length=250, verbose_name='product name')
    price = models.FloatField(verbose_name='product price')
    quantity = models.IntegerField(verbose_name='quantity currently available', null=True)
    # add images to categories

class HomepageSetup(models.Model):
    '''model for custom page Homepage Setup'''
    title = models.CharField(max_length=100, verbose_name='store name')
