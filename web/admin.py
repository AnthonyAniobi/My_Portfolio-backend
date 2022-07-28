from unicodedata import category
from django.contrib import admin

from web.models import category, work, education, experience

# Register your models here.
admin.site.register([
    category.Category,
    work.Work,
    education.Education,
    experience.Experience,
    ])