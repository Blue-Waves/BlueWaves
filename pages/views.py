from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from listing.choices import price_choices, category_choices, city_choices
from listing.models import Listing, SUB_CATEGORY_SELECT


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:8]

    # post = get_object_or_404(Listing, pk=px)
    # fav = bool
    # if post.favourites.filter(id=request.user.id).exists():
    #     fav = True
    sub_category_sum = []
    for sub_category_option in SUB_CATEGORY_SELECT:
        sub_category_sum += str(Listing.objects.filter(
            sub_category=sub_category_option[0]).count())

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'city_choices': city_choices,
        'category_choices': category_choices,
        'sub_category_sum': sub_category_sum,

        # 'fav': fav

    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')
