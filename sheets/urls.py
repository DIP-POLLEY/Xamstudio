from django.urls import path


from . import views
urlpatterns = [

    
   
    path('room',views.room, name='room'),
    path("rule",views.rule, name='rule'),
    path('xampage',views.xampage, name='xampage'),
    path('result1',views.result1,name='result1'),
    path('malpractice',views.malpractice,name='malpractice'),


]