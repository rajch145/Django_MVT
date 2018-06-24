from django.shortcuts import render
from UserApp.forms import NewUserForm
from UserApp.models import User
# Create your views here.

def index(request):
    return render(request, 'UserApp/index.html')

def user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('invalid form submitted')
            return render(request,'UserApp/user.html',{'form':form})

    return render(request,'UserApp/user.html',{'form':form})

def all_user(request):
    all_user = User.objects.order_by('first_name')
    user_dict = {'user_records':all_user}
    return render(request, 'UserApp/user_list.html',context=user_dict)
