from unicodedata import name
from django.urls import path
from django.conf.urls import handler404, handler500
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio', views.portfolio, name='portfolio'),
]

handler404 = 'web.views.not_found'
handler500 = 'web.views.server_error'