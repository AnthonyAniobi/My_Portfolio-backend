from django.db import models

class Experience(models.Model):
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    position = models.CharField(max_length=100, verbose_name='Position Held')
    company = models.CharField(max_length=250, verbose_name='Company Worked')
    description = models.TextField(verbose_name='A short description of company')
    current = models.BooleanField(default=False, verbose_name='Currently working here')

    def __str__(self) -> str:
        return self.company