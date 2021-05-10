from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Q
from django.core.exceptions import FieldError
from django.http import HttpResponse, Http404
from .models import Dish, Menu
from .serializers import DishSerializer, MenuSerializer

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics, viewsets
from rest_framework.parsers import FormParser, MultiPartParser


## list all existing dishes (all in database, menus irrelevant)
@api_view(['GET'])
def list_dishes(request, sort=None):
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
def retrieve_dish_details(request, pk):
    dish_instance = get_object_or_404(Dish, pk=pk)
    serializer = DishSerializer(dish_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


## list all menus (non empty, meaning with at least 1 Dish)
@api_view(['GET'])
def list_menus(request, sort=None):
    sort_param = request.GET.get('sort')
    # sort by count of foreign-key objects if asked for
    if sort_param in ['dishes']:
        try:
            queryset = Menu.objects.annotate(count_of_objects=Count(sort_param)) \
                                    .exclude(dishes=None) \
                                    .order_by('-count_of_objects')
        except FieldError:   # model does not have the parameter specified in a request
            queryset  = Menu.objects.exclude(dishes=None)
    # sort by regualar model's field if asked for
    elif sort_param not in ['dishes'] and sort_param != None:
        try:
            queryset = Menu.objects.exclude(dishes=None).order_by(sort_param)        # can add asc/desc parameter
        except FieldError:   # model does not have the parameter specified in a request
            queryset  = Menu.objects.exclude(dishes=None)
    else:   # do not sort, get non-empty menus (as for dishes)
        queryset  = Menu.objects.exclude(dishes=None)
    serializer = MenuSerializer(queryset , many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


## get details on a single menu
@api_view(['GET'])
def retrieve_menu_details(request, pk):
    menu_instance = get_object_or_404(Menu, pk=pk)
    serializer = MenuSerializer(menu_instance)
    return Response(serializer.data, status=status.HTTP_200_OK)


##  POST method for Dish model
# TODO cannot edit picture field
class DishCreateView(generics.CreateAPIView):
    serializer_class = DishSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user
    parser_classes = (FormParser, MultiPartParser)

    ## create one object
    def create(self, request, *args, **kwargs):
        # serialize user input
        serializer = DishSerializer(data=request.data)
        # validate user input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##  PUT and DELETE methods for Dish model
class DishView(generics.GenericAPIView):
    serializer_class = DishSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user
    parser_classes = (FormParser, MultiPartParser)      #  both FormParser and MultiPartParser together in order to fully support HTML form data.

    ## update one object (as a whole; use patch for partial update)
    def put(self, request, pk, format=None):
        # serialize user input
        serializer = DishSerializer(data=request.data)
        # validate user input, save changes to db if ok, return errors if not
        if serializer.is_valid():
            dish_instance = get_object_or_404(Dish, pk=pk)
            serializer.update(request.data, dish_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ## delete one object
    # TODO - remove unused old picture from static folder so it wont take space
    def delete(self, request, pk, format=None):
        dish_instance = get_object_or_404(Dish, pk=pk)
        dish_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##  POST method for Menu model
class MenuCreateView(generics.CreateAPIView):
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user

    ## create one object
    def create(self, request, *args, **kwargs):
        # serialize user input
        serializer = MenuSerializer(data=request.data)
        # validate user input, save to db if ok, return errors if not
        if serializer.is_valid():
            serializer.create(request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##  PUT and DELETE methods for Menu model
class MenuView(generics.GenericAPIView):
    serializer_class = MenuSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]	            # will deny permission to any unauthenticated user

    ## update one object (as a whole; use patch for partial update)
    def put(self, request, pk, format=None):
        # serialize user input
        serializer = MenuSerializer(data=request.data)
        # validate user input, save changes to db if ok, return errors if not
        if serializer.is_valid():
            menu_instance = get_object_or_404(Menu, pk=pk)
            serializer.update(request.data, menu_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ## delete one object
    def delete(self, request, pk, format=None):
        menu_instance = get_object_or_404(Menu, pk=pk)
        menu_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)