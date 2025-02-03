"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from employee.views import employee
from employee import views
from adminsignup.views import sign
from adminlogin.views import login
from employee.views import index_view
from employee.views import about_view
from employee.views import service_view
from employee.views import team_view


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('employee/',employee),
    path('show',views.show,name='show'),
    path('adminsignup/',sign),
   path('adminlogin/',login),
  
    path("index",index_view,name='index'),
    path("about",about_view,name='about'),
    path("service",service_view,name='service'),
    path("team",team_view,name='team'),
    
    
       
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
