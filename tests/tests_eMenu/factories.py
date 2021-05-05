'''
per app file to store factories
'''

from eMenu.models import Dish, Menu
import factory


class DishFactory(factory.django.DjangoModelFactory):
   
    class Meta:
        model = Dish

    name = 'Test Dish Name'
    description = 'Test dish description'
    price_in_dollars = 20
    minutes_to_prepare = 15
    is_vegetarian = False 