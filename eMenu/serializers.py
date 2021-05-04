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
            'pk',
            'name', 
            'description',
            'price_in_dollars',
            'minutes_to_prepare',
            'is_vegetarian',
            'picture',
            'creation_date',
            'edition_date')

        read_only_fields = ('pk', 'creation_date', 'edition_date')


    def update(self, validated_data, dish_instance):
        # update post info
        dish_instance.name = validated_data.get('name', dish_instance.name)
        dish_instance.description = validated_data.get('description', dish_instance.description)
        dish_instance.price_in_dollars = validated_data.get('price_in_dollars', dish_instance.price_in_dollars)
        dish_instance.minutes_to_prepare = validated_data.get('minutes_to_prepare', dish_instance.minutes_to_prepare)
        dish_instance.is_vegetarian = validated_data.get('is_vegetarian', dish_instance.is_vegetarian)
        dish_instance.picture = validated_data.get('picture', dish_instance.picture)
        dish_instance.update_edition_date()

        # save instance to db
        dish_instance.save()
        return dish_instance



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


    def update(self, validated_data, menu_instance):
        # update post info
        menu_instance.name = validated_data.get('name', menu_instance.name)
        menu_instance.description = validated_data.get('description', menu_instance.description)
        menu_instance.update_edition_date()

        # update Dishes
        dishes_data = validated_data.get('dishes')
        if dishes_data:
            menu_instance.dishes.clear()
            for dish in dishes_data:
                dish_qs = Tag.objects.filter(pk__iexact=dish['pk'])
                if dish_qs.exists():
                    menu_instance.dishes.add(dish_qs.first())
                else:
                    # just skip dish id that does not exist; could result in Menu with no Dish object
                    continue

        # save instance to db
        menu_instance.save()
        return menu_instance