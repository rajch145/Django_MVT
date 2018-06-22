from django.shortcuts import render
from mvt_app.models import User
import mvt_app
# Create your views here.

def index(request):
    return render(request, 'mvt_app/index.html',context={})

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_records':user_list}
    return render(request, 'mvt_app/users.html',context=user_dict)
