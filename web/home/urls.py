
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction

from home import views
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("service",views.service,name="service"),
    path("service",views.service,name="service"),
    path("employee",views.contact,name="employee"),
  
  
    
    path('signup/',signaction),
    path('login/',loginaction),
     
   
]
