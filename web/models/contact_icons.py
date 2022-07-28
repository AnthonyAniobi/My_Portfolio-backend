from django.db import models

class ContactIcons(models.Model):
    image_url= models.URLField(verbose_name='Url of Image')
    alt_text= models.CharField(max_length=100, verbose_name='alternative text of image')
    link = models.URLField(verbose_name='Link to Path')
    mail = models.BooleanField(default=False, verbose_name='is Email')