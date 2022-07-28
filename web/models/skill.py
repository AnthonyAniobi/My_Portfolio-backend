from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='name of skill')
    percentage = models.IntegerField(max_length=3, verbose_name='percentage of aptitude')
    isCoding = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name