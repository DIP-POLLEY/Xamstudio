from django.urls import path


from . import views
urlpatterns = [

    
   
    path('exam',views.exam, name='exam'),
    path('add_question',views.add_question, name='add_question'),


]