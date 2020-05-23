from django.urls import path


from . import views
urlpatterns = [

    
    path('',views.index, name='dashboard'),
    path('student',views.studashboard, name='studashboard'),


]