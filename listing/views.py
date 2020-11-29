from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from .choices import price_choices, category_choices, city_choices
from .forms import ListingForm, UpdateForm
from direct.models import Message
from Core.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


fav = bool


def listings(request):
    sort_condition = '-list_date'
    lowest_price = request.POST.get('submit-lowest-price')
    highest_price = request.POST.get('submit-highest-price')

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
                | Q(category__icontains=keywords))

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
    }
    return render(request, 'listings/search.html', context)


@login_required
def create(request):
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
        return render(request, 'listings/create.html', {'form': ListingForm()})


@login_required
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


@login_required
def delete_listing(request, pk):
    listing = Listing.objects.get(id=pk, owner=request.user)
    if request.method == "POST":
        listing.delete()
        messages.success(request, 'Item has been removed successfully')
        return redirect('dashboard')


@login_required
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
