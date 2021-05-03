from django.db import models
from django.utils import timezone


class Dish(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price_in_dollars = models.IntegerField()
    minutes_to_prepare = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    edition_date = models.DateTimeField(default=timezone.now, editable=True)
    is_vegetarian = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='dishes', default='dishes/default.jpg')
        
    ## return it in a way you want it to be printed out   
    def __str__(self):
        return f'Dish: {self.name}'


    # add checks/constraints like price_in_dollars > 0


class Menu(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    edition_date = models.DateTimeField(blank=True, null=True)
    dishes = models.ManyToManyField(Dish)

    ## return it in a way you want it to be printed out   
    def __str__(self):
        return f'Menu: {self.name}'
