from django.db import models

class Education(models.Model):
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date')
    course = models.CharField(max_length=250, verbose_name='Name of Course')
    school = models.CharField(max_length=500, verbose_name='Name of School')
    certificate_type = models.CharField(max_length=100, verbose_name='Type of Certificate')
    description = models.TextField(null=True, verbose_name='Description on education')

    def __str__(self) -> str:
        return self.school