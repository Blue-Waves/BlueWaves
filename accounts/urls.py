from django.urls import path
from . import views
from accounts.views import register, confirmregister
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView)

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('register/confirm', views.confirmregister, name="confirmregister"),
    path('logout/', views.userlogout, name="logout"),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/myinquiries', views.myinquiries, name='myinquiries'),
    path('dashboard/inquiry1', views.inquiry1, name='inquiry1'),
    path('dashboard/send_reply', views.send_reply, name="send_reply"),
    path('reset-password', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password/done', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('fav/<int:id>/', views.add_favourite, name='add_favourite'),
    #     path('unfav/<int:id>/', views.delete_favourite, name='delete_favourite'),
    path('favourites/', views.favourites_list, name='favourites_list')
]
