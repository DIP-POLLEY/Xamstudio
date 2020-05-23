from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.contrib.auth.models import Group

# Create your views here.
@unauthenticated_user
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd1 = request.POST['password1']
        user = auth.authenticate(username=uname,password=pwd1)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    else:
        return render(request,'loginpage.html')




@unauthenticated_user
def register(request):
    if request.method == 'POST':
        fstname = request.POST['firstname']
        lstname = request.POST['lastname']
        uname = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        
        if pwd1 == pwd2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username Not Available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')

            else :
                user = User.objects.create_user(username=uname,password=pwd1,email=email,first_name=fstname,last_name=lstname)
                user.save()
                group = Group.objects.get(name='student')
                user.groups.add(group)
                return render(request,'loginpage.html')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')


    else:
        return render(request,'registrationpage.html')


def logout(request):
    auth.logout(request)
    return redirect('/')