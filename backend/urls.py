import os
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(os.getenv('ADMIN_PATH'), admin.site.urls),
    path('', include('web.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',include('api.urls')),
]
