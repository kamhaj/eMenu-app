  
from django.urls import path, re_path
from . import views


app_name = 'short_texts'

urlpatterns = [
    ## API overview
	path('', views.api_overview, name='api-overview'),

    ## eMenu app dish/list_dishes?sort=name
    # Dish model CRUD
    re_path(r'^dish/list_dishes/$', views.get_dishes, name='list_dishes'),      # can be sorted be any field (e.g. name), e.g. http://localhost:8000/api/eMenu/menu/list_menus/?sort=dishes; http://localhost:8000/api/eMenu/dish/list_dishes/?sort=edition_date
    re_path(r'dish/dish_details(?P<pk>\w+|)/$', views.get_dish_details, name='get_dish_details'),

    # Menu model CRUD
    re_path(r'^menu/list_menus/$', views.get_menus, name='list_menus'),         # can be sorted be any field (e.g. number of dishes)
	re_path(r'menu/menu_details(?P<pk>\w+|)/$', views.get_menu_details, name='get_menu_details'),
]