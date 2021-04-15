import json
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
from Core.models import User
from direct.models import Message
from .forms import ListingForm, UpdateForm
from .choices import price_choices, category_choices, city_choices
from .modelchoices import category_options, city_options
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from .models import (Listing, get_electronics_strings, get_vehicles_strings,
                     get_home_garden_tools_strings, get_sports_outdoors_strings,
                     get_property_strings, get_fashion_beauty_strings,
                     get_hobbies_interests_strings, get_services_strings,
                     get_kids_baby_strings, get_farming_industrial_strings,
                     get_pets_strings, get_jobs_strings, SUB_CATEGORY_SELECT)


fav = bool


def listings(request):
    sort_condition = '-list_date'
    lowest_price = request.POST.get('submit-lowest-price')
    highest_price = request.POST.get('submit-highest-price')
    category_sum = []
    sub_category_sum = []
    city_sum = []
    for category_option in category_options:
        category_sum += str(Listing.objects.filter(
            category=category_option).count())
    for sub_category_option in SUB_CATEGORY_SELECT:
        sub_category_sum += str(Listing.objects.filter(
            sub_category=sub_category_option[0]).count())
    for city_option in city_options:
        city_sum += str(Listing.objects.filter(
            city=city_option).count())

        if lowest_price:
            sort_condition = 'price'
        elif highest_price:
            sort_condition = '-price'

    listings = Listing.objects.order_by(
        sort_condition).filter(is_published=True)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    # post = get_object_or_404(Listing, pk=1)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True

    context = {
        'listings': page_listings,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'category_sum': category_sum,
        'sub_category_sum': sub_category_sum,
        'city_sum': city_sum,



        # 'fav': fav,

    }

    return render(request, 'listings/listings.html', context)


def category_listings(request, category):
    sort_condition = '-list_date'
    lowest_price = request.POST.get('submit-lowest-price')
    highest_price = request.POST.get('submit-highest-price')

    if lowest_price:
        sort_condition = 'price'
    elif highest_price:
        sort_condition = '-price'

    category_sum = []
    city_sum = []
    for category_option in category_options:
        category_sum += str(Listing.objects.filter(
            category=category_option).count())
    for city_option in city_options:
        city_sum += str(Listing.objects.filter(
            city=city_option).count())
    # Change Vehicels spelling
    listings = Listing.objects.order_by(
        sort_condition).filter(is_published=True, category=category)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    # post = get_object_or_404(Listing, pk=1)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True

    context = {
        'listings': page_listings,
        'category': category,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'category_sum': category_sum,
        'city_sum': city_sum,
        # 'fav': fav,

    }

    return render(request, 'listings/filtered_listings.html', context)


def sub_category_listings(request, sub_category):
    sort_condition = '-list_date'
    lowest_price = request.POST.get('submit-lowest-price')
    highest_price = request.POST.get('submit-highest-price')

    if lowest_price:
        sort_condition = 'price'
    elif highest_price:
        sort_condition = '-price'

    category_sum = []
    city_sum = []
    for category_option in category_options:
        category_sum += str(Listing.objects.filter(
            category=category_option).count())
    for city_option in city_options:
        city_sum += str(Listing.objects.filter(
            city=city_option).count())
    # Change Vehicels spelling
    listings = Listing.objects.order_by(
        sort_condition).filter(is_published=True, sub_category=sub_category)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    # post = get_object_or_404(Listing, pk=1)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True

    context = {
        'listings': page_listings,
        'sub_category': sub_category,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'category_sum': category_sum,
        'city_sum': city_sum,
        # 'fav': fav,

    }

    return render(request, 'listings/filtered_listings.html', context)


def city_listings(request, city):

    sort_condition = '-list_date'
    lowest_price = request.POST.get('submit-lowest-price')
    highest_price = request.POST.get('submit-highest-price')

    if lowest_price:
        sort_condition = 'price'
    elif highest_price:
        sort_condition = '-price'

    category_sum = []
    city_sum = []
    for category_option in category_options:
        category_sum += str(Listing.objects.filter(
            category=category_option).count())
    for city_option in city_options:
        city_sum += str(Listing.objects.filter(
            city=city_option).count())

    listings = Listing.objects.order_by(
        sort_condition).filter(is_published=True, city=city)
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    # post = get_object_or_404(Listing, pk=1)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True

    context = {
        'listings': page_listings,
        'city': city,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'category_sum': category_sum,
        'city_sum': city_sum,

        # 'fav': fav,

    }

    return render(request, 'listings/filtered_listings.html', context)


def listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    post = get_object_or_404(Listing, pk=pk)
    fav = bool
    if post.favourites.filter(id=request.user.id).exists():
        fav = True
    context = {
        'listing': listing,
        'fav': fav,

    }
    return render(request, 'listings/listing.html', context)


def search(request):
    search_query = ''
    category_query = ''
    price_query = ''
    city_query = ''

    query_set = Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        search_query = request.GET['keywords']
        if keywords:
            query_set = query_set.filter(
                Q(description__icontains=keywords) | Q(
                    title__icontains=keywords) | Q(city__icontains=keywords)
                | Q(category__icontains=keywords) | Q(sub_category__icontains=keywords))

    if 'category' in request.GET:
        category = request.GET['category']
        category_query = request.GET['category']
        if category:
            query_set = query_set.filter(category__iexact=category)

    if 'city' in request.GET:
        city = request.GET['city']
        city_query = request.GET['city']
        if city:
            query_set = query_set.filter(city__iexact=city)

    if 'price' in request.GET:
        price = request.GET['price']
        price_query = request.GET['price']
        if price:
            query_set = query_set.filter(price__lte=price)
    category_sum = []
    city_sum = []
    for category_option in category_options:
        category_sum += str(Listing.objects.filter(
            category=category_option).count())
    for city_option in city_options:
        city_sum += str(Listing.objects.filter(
            city=city_option).count())

    context = {
        'query_set': query_set,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'values': request.GET,
        'search_query': search_query,
        'category_query': category_query,
        'city_query': city_query,
        'price_query': price_query,
        'category_sum': category_sum,
        'city_sum': city_sum,
    }
    return render(request, 'listings/search.html', context)


@login_required
def create(request):
    electronics_strings = get_electronics_strings()
    vehicles_strings = get_vehicles_strings()
    home_garden_tools_strings = get_home_garden_tools_strings()
    sports_outdoors_strings = get_sports_outdoors_strings()
    property_strings = get_property_strings()
    fashion_beauty_strings = get_fashion_beauty_strings()
    hobbies_interests_strings = get_hobbies_interests_strings()
    services_strings = get_services_strings()
    kids_baby_strings = get_kids_baby_strings()
    farming_industrial_strings = get_farming_industrial_strings()
    pets_strings = get_pets_strings()
    jobs_strings = get_jobs_strings()

    json_electronics_strings = json.dumps(electronics_strings)
    json_vehicles_strings = json.dumps(vehicles_strings)
    json_home_garden_tools_strings = json.dumps(home_garden_tools_strings)
    json_sports_outdoors_strings = json.dumps(sports_outdoors_strings)
    json_property_strings = json.dumps(property_strings)
    json_fashion_beauty_strings = json.dumps(fashion_beauty_strings)
    json_hobbies_interests_strings = json.dumps(hobbies_interests_strings)
    json_services_strings = json.dumps(services_strings)
    json_kids_baby_strings = json.dumps(kids_baby_strings)
    json_farming_industrial_strings = json.dumps(farming_industrial_strings)
    json_pets_strings = json.dumps(pets_strings)
    json_jobs_strings = json.dumps(jobs_strings)

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.owner = request.user
            new.save()
            messages.success(request, "Item is now live!")
            return redirect('dashboard')
        else:
            pass
    else:
        context = {'form': ListingForm(),
                   'json_electronics_strings': json_electronics_strings,
                   'json_vehicles_strings': json_vehicles_strings,
                   'json_home_garden_tools_strings': json_home_garden_tools_strings,
                   'json_sports_outdoors_strings': json_sports_outdoors_strings,
                   'json_property_strings': json_property_strings,
                   'json_fashion_beauty_strings': json_fashion_beauty_strings,
                   'json_hobbies_interests_strings': json_hobbies_interests_strings,
                   'json_services_strings': json_services_strings,
                   'json_kids_baby_strings': json_kids_baby_strings,
                   'json_farming_industrial_strings': json_farming_industrial_strings,
                   'json_pets_strings': json_pets_strings,
                   'json_jobs_strings': json_jobs_strings, }
        return render(request, 'listings/create.html', context)


@ login_required
def update(request, pk):
    listing = Listing.objects.get(id=pk, owner=request.user)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            messages.success(request, "Item has been updated")
            return redirect('dashboard')
    context = {
        'form': UpdateForm(instance=listing),
        'update': True
    }

    return render(request, 'listings/create.html',  context)


@ login_required
def delete_listing(request, pk):
    listing = Listing.objects.get(id=pk, owner=request.user)
    if request.method == "POST":
        listing.delete()
        messages.success(request, 'Item has been removed successfully')
        return redirect('dashboard')


@ login_required
def NewConversation(request, username):
    from_user = request.user
    body = 'Wagwan'
    try:
        to_user = User.objects.get(username=username)
    except Exception as e:
        return redirect('usersearch')
    if from_user != to_user:
        Message.send_message(from_user, to_user, body)
    return redirect('inbox')
