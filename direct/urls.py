from django.urls import path
from .views import inbox, Directs, SendDirect, UserSearch, NewConversation

urlpatterns = [
    path('direct/', inbox, name='inbox'),
    path('directs/<username>', Directs, name='directs'),
    path('send/', SendDirect, name='send_direct'),
    path('new/', UserSearch, name='usersearch'),
    path('new/<username>', NewConversation, name='newconversation'),
]