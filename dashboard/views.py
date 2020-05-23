from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user,allowed_users,admin_only

# Create your views here.



@login_required(login_url='accounts/login')
# @allowed_users(allowed_roles='teacher')
@admin_only
def index(request):
    return render(request,"dashboard.html")



@login_required(login_url='accounts/login')
# @allowed_users(allowed_roles='student')
def studashboard(request):
    return render(request,"studashboard.html")