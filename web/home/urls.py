
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction

from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("employee",views.contact,name="employee"),
  
  
    
    path('signup/',signaction),
    path('login/',loginaction),
     
   
]
