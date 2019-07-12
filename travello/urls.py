from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('mumbai.html',views.mumbai,name='mumbai'),
    path('pune.html',views.pune,name='pune'),
    path('hyderabad.html',views.hyderabad,name='hyderabad'),
    path('bengaluru.html',views.bengaluru,name='bengaluru'),

]