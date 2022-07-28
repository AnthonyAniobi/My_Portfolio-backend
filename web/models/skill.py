from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='name of skill')
    percentage = models.IntegerField(min=0, max=100, verbose_name='percentage of aptitude')