from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from listing.choices import price_choices, category_choices, city_choices
from listing.models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)
    # post = get_object_or_404(Listing, pk=px)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        # 'fav': fav

    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
