from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views
from .models import *


app_name = 'eMenu'


urlpatterns = [
    ## eMenu regular views
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    re_path(r'^dish/list_dishes/$', views.list_dishes, name='list_dishes'), 
    re_path(r'^dish/list_menus/$', views.list_menus, name='list_menus'), 
]