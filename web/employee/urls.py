from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from django.conf import settings
from django.conf.urls.static import static
from employee import views
from adminsignup.views import sign
from adminlogin.views import login
from .views import index_view


urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("services",views.services,name="services"),
    path("employee",views.employee,name="employee"),
    path("adminsignup/",sign),
    path("adminlogin",login),
    path('signup/',signaction),
    path('login/',loginaction),
    path('show', views.show),
    path("",index_view,name='index'),
    
    
     
   
]+static(settings.MEDIA_URL,document_roots=settings.MEDIA_ROOT)

    