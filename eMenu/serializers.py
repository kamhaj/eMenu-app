''' To make our objects available through the API, we need to perform a serialization – reflect the data 
contained in the object textually. The default format here is JSON, although DRF allows serialization to XML or YAML
'''

from rest_framework import serializers
from .models import *


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        # model to be serialized
        model = Dish 					
        # fields to be displayed
        fields = (
            'name', 
            'description',
            'price_in_dollars',
            'minutes_to_prepare',
            'is_vegetarian',
            'picture',
            'creation_date',
            'edition_date')

        read_only_fields = ('pk', 'creation_date', 'edition_date')


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(read_only=True, many=True)

    class Meta:
        # model to be serialized
        model = Menu 					
        # fields to be displayed (dishes in a form of list of integers)
        fields = (
            'name', 
            'description',
            'creation_date',
            'edition_date',
            'dishes')

        read_only_fields = ('pk', 'creation_date', 'edition_date')
