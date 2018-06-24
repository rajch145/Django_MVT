from django.urls import path
from UserApp import views

app_name = 'UserApp'

urlpatterns = [

path('', views.user,name = 'user' ),
path('users/',views.all_user, name='all_users'),
]
