from django.contrib import admin

from web.models import category, work, education, experience, contact_icons

# Register your models here.
admin.site.register([
    category.Category,
    work.Work,
    education.Education,
    experience.Experience,
    contact_icons.ContactIcons,
    ])