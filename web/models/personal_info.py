from django.db import models

class PersonalInfo(models.Model):
    image = models.URLField(verbose_name='my image url')
    age = models.IntegerField(verbose_name='my age')
    complete_adress = models.TextField(verbose_name='my adress')
    short_adress = models.CharField(max_length=250, verbose_name='consise adress')
    phone_line1 = models.IntegerField(verbose_name='first phone number')
    phone_line2 = models.IntegerField(verbose_name='second phone number')
    github_link = models.URLField(null=True, verbose_name='github profile link')
    linkedin_link = models.URLField(null=True, verbose_name='linkedin profile link')
    codeCanyon_link = models.URLField(null=True, verbose_name='code canyon profile link')
    facebook_link = models.URLField(null=True, verbose_name='facebook profile link')
    playstore_link = models.URLField(null=True, verbose_name='playstore profile link')
    fiverr_link = models.URLField(null=True, verbose_name='fiverr profile link')
    upwork_link = models.URLField(null=True, verbose_name='upwork profile link')
    gmail_link = models .EmailField(null=True, verbose_name='gmail profile link')
    copyright = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return 'MyProfile at age: '+str(self.age)