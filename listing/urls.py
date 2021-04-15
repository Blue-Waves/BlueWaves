from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('<category>',
         views.category_listings, name='category_listings'),
    path('city_listings/<city>',
         views.city_listings, name='city_listings'),
    path('sub_category_listings/<sub_category>',
         views.sub_category_listings, name='sub_category_listings'),
    path('<int:pk>/', views.listing, name='listing'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete_listing, name="delete"),
    path('new/<username>', views.NewConversation, name='newconversations'),
]
