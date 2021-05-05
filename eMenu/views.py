from django.shortcuts import render
from .models import Dish, Menu


## Home Page
def home(request):
        ## we can use arguments from context, we refer to them in HTML template by key names
        context = {
            'dishes': Dish.objects.all()
        }
        return render(request, 'home.html', context)

## About Page
def about(request):
        return render(request, 'about.html', {'title': 'About'})

    
## list dishes
def list_dishes(request):
        ## we can use arguments from context, we refer to them in HTML template by key names
        context = {
            'dishes': Dish.objects.all()
        }
        return render(request, 'eMenu/list_dishes.html', context)


## list menus
def list_menus(request):
        ## we can use arguments from context, we refer to them in HTML template by key names
        context = {
            'menus': Menu.objects.all()
        }
        return render(request, 'eMenu/list_menus.html', context)