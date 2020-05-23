from django.urls import path
from django.contrib.auth import views as auth_views



from . import views



urlpatterns = [

    
    path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),


    
      path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="mail.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="sentmail.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="rstpwd.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="pwdreseted.html"), 
        name="password_reset_complete"),

]