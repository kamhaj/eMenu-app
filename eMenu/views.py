from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from rest_framework import status

from .serializers import DishSerializer, MenuSerializer
from django.db.models import Count
from .models import Dish, Menu
from django.core.exceptions import FieldError

import json



@api_view(['GET'])
def api_overview(request):
	api_urls = {
        'GET list of all dishes': '/api/eMenu/dish/list_dishes',
		'GET dish details': '/api/eMenu/dish/dish_details/<int:pk>',
        'GET list of all menus': '/api/eMenu/menu/menu_dishes',
		'GET menu details': '/api/eMenu/menu/menu_details/<int:pk>',
	}

	return Response(api_urls)


## list all existing dishes (all in database, menus irrelevant)
@api_view(['GET'])
def get_dishes(request, sort=None):
    sort_param = request.GET.get('sort')
    # sort by parameter if asked for
    try:
        queryset = Dish.objects.order_by(sort_param)        # can add asc/desc parameter
    except FieldError:   # model does not have the parameter specified in a request
        queryset  = Dish.objects.all()    
    serializer = DishSerializer(queryset , many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


## get details on a single dish
@api_view(['GET'])
def get_dish_details(request, pk):
    dish_instance = get_object_or_404(Dish, pk=pk)
    serializer = DishSerializer(dish_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


## list all menus
@api_view(['GET'])
def get_menus(request, sort=None):
    sort_param = request.GET.get('sort')
    # sort by count of foreign-key objects if asked for
    if sort_param in ['dishes']:
        try:
            queryset = Menu.objects.annotate(count_of_objects=Count(sort_param)) \
                                    .order_by('-count_of_objects')
        except FieldError:   # model does not have the parameter specified in a request
            queryset  = Menu.objects.all()
    # sort by regualar model's field if asked for
    elif sort_param not in ['dishes']:
        try:
            queryset = Menu.objects.order_by(sort_param)        # can add asc/desc parameter
        except FieldError:   # model does not have the parameter specified in a request
            queryset  = Menu.objects.all()    
    # do not sort
    else: 
        queryset  = Menu.objects.all()    
    serializer = MenuSerializer(queryset , many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


## get details on a single menu
@api_view(['GET'])
def get_menu_details(request, pk):
    menu_instance = get_object_or_404(Menu, pk=pk)
    serializer = MenuSerializer(menu_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)



class DishView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user

    ## create one object
    def post(self, request, format=None):
        pass

    ## update one object (as a whole; use patch for partial update)
    def put(self, request, format=None):
        pass

    ## delete one object
    def delete(self, request, format=None):
        pass


class MenuView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user

    ## create one object
    def post(self, request, format=None):
        pass

    ## update one object (as a whole; use patch for partial update)
    def put(self, request, format=None):
        pass

    ## delete one object
    def delete(self, request, format=None):
        pass