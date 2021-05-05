'''
unit tests examples for testing models
testing models is basically checking if we can work with the model (CRUD operations)
if some default methods (e.g. save()) were overridden, then they should be tested too
'''

from eMenu.models import Dish
from .factories import DishFactory
import pytest


@pytest.mark.django_db
class TestDishModel():   

    def test_create_new_dish(self):
        dish = DishFactory.create() # saves it to db; use build() for no save
        # Check all field and validators
        dish.clean_fields()  #  EXCLUDE: FK, O2O, M2M Fields
        
        # Check if at least one Post is present (can be more, it depends on test order if we do not delete new instances in tests)
        dishes = Dish.objects.all()
        assert len(dishes) >= 1
        
        
    def test_check_attribute_in_dish(self):
        # Check attributes
        dish = DishFactory()
        assert dish.name == 'Test Dish Name'
        assert dish.description == 'Test dish description'
        assert dish.price_in_dollars == 20
        assert dish.minutes_to_prepare == 15
        assert dish.is_vegetarian == False


    def test_check_str_representation_of_dish(self):
        # Check string representation
        dish = DishFactory(name="New Dish Name", description='New dish description')
        assert dish.__str__() == 'New Dish Name'