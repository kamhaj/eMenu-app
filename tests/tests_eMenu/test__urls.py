'''
test if invoking a certain URL will trigger given class/view function.
'''


from django.urls import reverse, resolve
from eMenu.models import Dish, Menu
from eMenu import api_views, views

class TestGeneralUrls():
    def test_home_url(self):
        #found = resolve(reverse('eMenuAPI:retrieve_dish_details', kwargs={'pk': '1'}))
        found = resolve(reverse('eMenu:home'))
        print(found)
        assert found.func == views.home

    def test_home_url(self):
        #found = resolve(reverse('eMenuAPI:retrieve_dish_details', kwargs={'pk': '1'}))
        found = resolve(reverse('eMenu:about'))
        print(found)
        assert found.func == views.about


class TestDishURLs():

    def test_dish_list_url(self):
        found = resolve(reverse('eMenu:list_dishes'))
        print(found)
        assert found.func == views.list_dishes


class MenuDishURLs():

    def test_menu_list_url(self):
        found = resolve(reverse('eMenu:list_menus'))
        print(found)
        assert found.func == views.list_menus


class TestDishApiUrls():

    def test_dish_details_url(self):
        found = resolve(reverse('eMenuAPI:retrieve_dish_details', kwargs={'pk': '1'}))
        print(found)
        assert found.func == api_views.retrieve_dish_details

    def test_dish_creation_url(self):
        found = resolve(reverse('eMenuAPI:create-dish'))
        print(found)
        assert found.func.view_class == api_views.DishCreateView

    def test_dish_update_url(self):
        found = resolve(reverse('eMenuAPI:update-delete-dish', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == api_views.DishView

    def test_dish_deletion_url(self):
        found = resolve(reverse('eMenuAPI:update-delete-dish', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == api_views.DishView

    

class TestMenuApiUrls():

    def test_menu_details_url(self):
        found = resolve(reverse('eMenuAPI:retrieve_menu_details', kwargs={'pk': '1'}))
        print(found)
        assert found.func == api_views.retrieve_menu_details

    def test_menu_creation_url(self):
        found = resolve(reverse('eMenuAPI:create-menu'))
        print(found)
        assert found.func.view_class == api_views.MenuCreateView

    def test_menu_update_url(self):
        found = resolve(reverse('eMenuAPI:update-delete-menu', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == api_views.MenuView

    def test_menu_deletion_url(self):
        found = resolve(reverse('eMenuAPI:update-delete-menu', kwargs={'pk': '1'}))
        print(found)
        assert found.func.view_class == api_views.MenuView