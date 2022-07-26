from django.contrib import admin
from .models import Product, Categories, HomepageSetup

admin.site.register([Product, Categories, HomepageSetup])
