from django.db import models
from datetime import datetime
from Core.models import User
from .choices import category_choices, city_choices
from .modelchoices import category_options
from django.conf import settings

ACTION = 'Action'
ADVENUTURE = 'Adventure'
RACING = 'Racing'
SPORTS = 'Sports'
SIMULATION = 'Simulation'
CONSOLES = 'Consoles'
ACCESSORIES = 'Accessories'
SERVICES = 'Services'
OPEN_WORLD = 'Open World'
FARMING_INDUSTRIAL = 'Farming & Industrial'
PETS = 'Pets'
JOBS = 'Jobs'


CATEGORY_SELECT = [
    (ACTION, ACTION),
    (ADVENUTURE, ADVENUTURE),
    (RACING, RACING),
    (SPORTS, SPORTS),
    (SIMULATION, SIMULATION),
    (CONSOLES, CONSOLES),
    (ACCESSORIES, ACCESSORIES),
    (SERVICES, SERVICES),
    (OPEN_WORLD, OPEN_WORLD),
    (FARMING_INDUSTRIAL, FARMING_INDUSTRIAL),
    (PETS, PETS),
    (JOBS, JOBS),
]


class Listing(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_SELECT)

    address = models.TextField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=255)
    price = models.IntegerField()
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d')
    photo_1 = models.ImageField(upload_to='None', blank=True)
    photo_2 = models.ImageField(upload_to='None', blank=True)
    photo_3 = models.ImageField(upload_to='None', blank=True)
    photo_4 = models.ImageField(upload_to='None', blank=True)
    photo_5 = models.ImageField(upload_to='None', blank=True)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title

# class Fav(models.Model):
#     listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         unique_together = ('thing', 'user')

#     def __str__(self):
#         return '%s likes %s'(self.user.username, self.listing.title[:10])
