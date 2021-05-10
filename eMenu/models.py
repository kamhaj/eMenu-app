from django.db import models
from django.utils import timezone
from PIL import Image
import os

STATIC_FILES_PATH = os.path.join(os.getcwd(), 'media/dishes')


class Dish(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    price_in_dollars = models.IntegerField()
    minutes_to_prepare = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    edition_date = models.DateTimeField(default=timezone.now, editable=True)
    is_vegetarian = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='dishes', default='dishes/default.jpg')       # TODO needs some sort of encoding probably

    ## change edition date (e.g. on update)
    def update_edition_date(self):
        self.edition_date = timezone.now()
        self.save()


    ## override parent class save method so we can resize images
    def save(self, *args, **kwargs):
        super().save()

        ## open current Profile instance's picture
        img =  Image.open(self.picture.path)

        ## resize if too big
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)   ## save to the same path
        
    ## return it in a way you want it to be printed out   
    def __str__(self):
        return f'{self.name}'

    # can add checks/constraints like price_in_dollars > 0


class Menu(models.Model):
    name = models.CharField(max_length=60, unique=True)     # could be a primary key
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=timezone.now, editable=False)
    edition_date = models.DateTimeField(default=timezone.now, editable=True)
    dishes = models.ManyToManyField(Dish)           # TODO if Dish gets deleted it can lead to empty Menu. We should do sth about it?

    ## change edition date (e.g. on update)
    def update_edition_date(self):
        self.edition_date = timezone.now()
        self.save()
        
    ## return it in a way you want it to be printed out   
    def __str__(self):
        return f'{self.name}'
