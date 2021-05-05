from django.urls import re_path
from rest_framework.routers import DefaultRouter
from . import api_views
from .models import *


app_name = 'eMenu'


urlpatterns = [
    ## eMenu API
    # Dish model CRUD
    re_path(r'^dish/list_dishes/$', api_views.list_dishes, name='list_dishes'),      # can be sorted be any field (e.g. name), e.g. http://localhost:8000/api/eMenu/menu/list_menus/?sort=dishes; http://localhost:8000/api/eMenu/dish/list_dishes/?sort=edition_date
    re_path(r'^dish/dish_details/(?P<pk>\w+)/$', api_views.retrieve_dish_details, name='retrieve_dish_details'),
    re_path(r'^dish/(?P<pk>\w+)/$', api_views.DishView.as_view(), name='update-delete-dish'),
    re_path(r'^dish/$', api_views.DishCreateView.as_view(), name='create-dish'),

    # Menu model CRUD
    re_path(r'^menu/list_menus/$', api_views.list_menus, name='list_menus'),         # can be sorted be any field (e.g. number of dishes)
	re_path(r'^menu/menu_details(?P<pk>\w+)/$', api_views.retrieve_menu_details, name='retrieve_menu_details'),
    re_path(r'^menu/(?P<pk>\w+)/$', api_views.MenuView.as_view(), name='update-delete-menu'),
    re_path(r'^menu/$', api_views.MenuCreateView.as_view(), name='create-menu'),
]

#  non-capturing group in the regex:        (?:/(?P<title>[a-zA-Z]+)/)?