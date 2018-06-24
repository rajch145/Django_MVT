from django.urls import path
from UserApp import views

urlpatterns = [

path('', views.user,name = 'user' ),
path('users/',views.all_user, name='all_users'),
]
