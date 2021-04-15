from django.db import models
from datetime import datetime
from Core.models import User
from .choices import category_choices, city_choices
from .modelchoices import category_options
from django.conf import settings

ELECTRONICS = 'Electronics'
VEHICLES = 'Vehicles'
HOME_GARDEN_TOOLS = 'Home & Garden Tools'
SPORTS_OUTDOORS = 'Sports & Outdoors Equipment'
PROPERTY = 'Property'
FASHION_BEAUTY = 'Fashion & Beauty'
HOBBIES_INTERESTS = 'Hobbies & Interests'
SERVICES = 'Services'
KIDS_BABY = 'Kids & Baby'
FARMING_INDUSTRIAL = 'Farming & Industrial'
PETS = 'Pets'
JOBS = 'Jobs'

PHONES = 'Phones'
CARS = 'Cars'
CAR_ACCESSORIES = 'Car Accessories'
MOTORCYCLES_SCOOTERS = 'Motorcycles and Scooters'
TRUCKS = 'Trucks'
BOATS = 'Boats'
CARAVANS = 'Caravans'
TV = 'TV'
COMPUTER_LAPTOPS = 'Computer & Laptops'
GAMING_CONSOLES = 'Gaming Consoles'
COMPUTER_HARDWARE_ACCESSORIES = 'Computer Hardware & Accessories'
CAMERAS = 'Cameras'
FURNITURE_DECOR = 'Furniture and Decor'
HOMEWARE_APPLIANCES = 'Homeware Appliances'
TOOLS_DIY = 'Tools & DIY'
GARDEN_BRAAI = 'Garden & Braai'
OUTDOOR_EQUIPMENT = 'Outdoor Equipment'
BICYCLES = 'Bicycles'
GYM_FITNESS = 'Gym Fitness'
HOUSES_FLATS_RENT = 'Houses & Flats for Rent'
HOUSES_FLATS_SALE = 'Houses & Flats for Sale'
LAND = 'Land'
OFFICE_SPACE = 'Office Space'
VACATION_RENTALS = 'Vacation Rentals'
CLOTHING_SHOES = 'Clothing & Shoes'
JEWELLERY_ACCESSORIES = 'Jewellery & Accessories'
HEALTH_BEAUTY_COSMETICS = 'Health, Beauty & Cosmetics'
TOYS_GAMES = 'Toys & Games'
MUSICAL_INSTRUMENTS = 'Musical Instruments'
ART = 'Art'
BOOKS_CDS_DVDS = 'Books, CDs, DVDs'
CONSTRUCTION = 'Construction'
OTHER_SERVICES = 'Other Services'
EVENT_SERVICES = 'Event Services'
TRANSPORT = 'Transport'
REPAIRS = 'Repairs'
DOMESTIC_HELP = 'Domestic Help'
PRAMS_COTS = 'Prams & Cots'
TODLER_CLOTHING_ACCESSORIES = 'Todler Clothing & Accessories'
FARMING_VEHICLES = 'Farming Vehicles'
LIVESTOK = 'Livestock'
FARMING_EQUIPMENT = 'Farming Equipment'
FEEDS_SUPPLEMENTS_SEEDS = 'Feeds, Supplements & Seeds'
DOGS_CATS = 'Dogs, Cats'
OTHER_PETS = 'Other Pets'
PET_ACCESSORIES = 'Pet Accessories'
JOB_OPPORTUNITIES = 'Job Opportunities'
CVS_RESUMES = 'CVs & Resumes'

CATEGORY_SELECT = [
    (ELECTRONICS, ELECTRONICS),
    (VEHICLES, VEHICLES),
    (HOME_GARDEN_TOOLS, HOME_GARDEN_TOOLS),
    (SPORTS_OUTDOORS, SPORTS_OUTDOORS),
    (PROPERTY, PROPERTY),
    (FASHION_BEAUTY, FASHION_BEAUTY),
    (HOBBIES_INTERESTS, HOBBIES_INTERESTS),
    (SERVICES, SERVICES),
    (KIDS_BABY, KIDS_BABY),
    (FARMING_INDUSTRIAL, FARMING_INDUSTRIAL),
    (PETS, PETS),
    (JOBS, JOBS),
]

SUB_CATEGORY_SELECT = [
    (PHONES, PHONES),
    (TV, TV),
    (COMPUTER_LAPTOPS, COMPUTER_LAPTOPS),
    (GAMING_CONSOLES, GAMING_CONSOLES),
    (COMPUTER_HARDWARE_ACCESSORIES, COMPUTER_HARDWARE_ACCESSORIES),
    (CAMERAS, CAMERAS),
    (CARS, CARS),
    (CAR_ACCESSORIES, CAR_ACCESSORIES),
    (MOTORCYCLES_SCOOTERS, MOTORCYCLES_SCOOTERS),
    (TRUCKS, TRUCKS),
    (BOATS, BOATS),
    (CARAVANS, CARAVANS),
    (JOB_OPPORTUNITIES, JOB_OPPORTUNITIES),
    (CVS_RESUMES, CVS_RESUMES),
    (FURNITURE_DECOR, FURNITURE_DECOR),
    (HOMEWARE_APPLIANCES, HOMEWARE_APPLIANCES),
    (TOOLS_DIY, TOOLS_DIY),
    (GARDEN_BRAAI, GARDEN_BRAAI),
    (OUTDOOR_EQUIPMENT, OUTDOOR_EQUIPMENT),
    (BICYCLES, BICYCLES),
    (GYM_FITNESS, GYM_FITNESS),
    (HOUSES_FLATS_RENT, HOUSES_FLATS_RENT),
    (HOUSES_FLATS_SALE, HOUSES_FLATS_SALE),
    (LAND, LAND),
    (OFFICE_SPACE, OFFICE_SPACE),
    (VACATION_RENTALS, VACATION_RENTALS),
    (CLOTHING_SHOES, CLOTHING_SHOES),
    (JEWELLERY_ACCESSORIES, JEWELLERY_ACCESSORIES),
    (HEALTH_BEAUTY_COSMETICS, HEALTH_BEAUTY_COSMETICS),
    (TOYS_GAMES, TOYS_GAMES),
    (MUSICAL_INSTRUMENTS, MUSICAL_INSTRUMENTS),
    (ART, ART),
    (BOOKS_CDS_DVDS, BOOKS_CDS_DVDS),
    (CONSTRUCTION, CONSTRUCTION),
    (OTHER_SERVICES, OTHER_SERVICES),
    (EVENT_SERVICES, EVENT_SERVICES),
    (TRANSPORT, TRANSPORT),
    (REPAIRS, REPAIRS),
    (DOMESTIC_HELP, DOMESTIC_HELP),
    (PRAMS_COTS, PRAMS_COTS),
    (TODLER_CLOTHING_ACCESSORIES, TODLER_CLOTHING_ACCESSORIES),
    (FARMING_VEHICLES, FARMING_VEHICLES),
    (LIVESTOK, LIVESTOK),
    (FARMING_EQUIPMENT, FARMING_EQUIPMENT),
    (FEEDS_SUPPLEMENTS_SEEDS, FEEDS_SUPPLEMENTS_SEEDS),
    (DOGS_CATS, DOGS_CATS),
    (OTHER_PETS, OTHER_PETS),
    (PET_ACCESSORIES, PET_ACCESSORIES),


]


def get_electronics_strings():
    electronics_strings = [
        PHONES,
        TV,
        COMPUTER_LAPTOPS,
        GAMING_CONSOLES,
        COMPUTER_HARDWARE_ACCESSORIES,
        CAMERAS,
    ]

    return electronics_strings


def get_vehicles_strings():
    vehicles_strings = [
        CARS,
        CAR_ACCESSORIES,
        MOTORCYCLES_SCOOTERS,
        TRUCKS,
        BOATS,
        CARAVANS,
    ]

    return vehicles_strings


def get_home_garden_tools_strings():
    home_garden_tools_strings = [
        FURNITURE_DECOR,
        HOMEWARE_APPLIANCES,
        TOOLS_DIY,
        GARDEN_BRAAI,
    ]

    return home_garden_tools_strings


def get_sports_outdoors_strings():
    sports_outdoors_strings = [
        OUTDOOR_EQUIPMENT,
        BICYCLES,
        GYM_FITNESS,
    ]

    return sports_outdoors_strings


def get_property_strings():
    property_strings = [
        HOUSES_FLATS_RENT,
        HOUSES_FLATS_SALE,
        LAND,
        OFFICE_SPACE,
        VACATION_RENTALS,
    ]

    return property_strings


def get_fashion_beauty_strings():
    fashion_beauty_strings = [
        CLOTHING_SHOES,
        JEWELLERY_ACCESSORIES,
        HEALTH_BEAUTY_COSMETICS,
    ]

    return fashion_beauty_strings


def get_hobbies_interests_strings():
    hobbies_interests_strings = [
        TOYS_GAMES,
        MUSICAL_INSTRUMENTS,
        ART,
        BOOKS_CDS_DVDS,
    ]

    return hobbies_interests_strings


def get_services_strings():
    services_strings = [
        CONSTRUCTION,
        OTHER_SERVICES,
        EVENT_SERVICES,
        TRANSPORT,
        REPAIRS,
        DOMESTIC_HELP,
    ]

    return services_strings


def get_kids_baby_strings():
    kids_baby_strings = [
        PRAMS_COTS,
        TODLER_CLOTHING_ACCESSORIES,
    ]

    return kids_baby_strings


def get_farming_industrial_strings():
    farming_industrial_strings = [
        FARMING_VEHICLES,
        LIVESTOK,
        FARMING_EQUIPMENT,
        FEEDS_SUPPLEMENTS_SEEDS,
    ]

    return farming_industrial_strings


def get_pets_strings():
    pets_strings = [
        DOGS_CATS,
        OTHER_PETS,
        PET_ACCESSORIES,
    ]

    return pets_strings


def get_jobs_strings():
    jobs_strings = [
        JOB_OPPORTUNITIES,
        CVS_RESUMES,
    ]

    return jobs_strings


class Listing(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_SELECT)
    sub_category = models.CharField(
        max_length=255, default='empty', choices=SUB_CATEGORY_SELECT)
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
