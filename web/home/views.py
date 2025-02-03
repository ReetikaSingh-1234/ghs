from django.shortcuts import render,HttpResponse
from datetime import datetime
from employee.models import Employee1
# Create your views here.

def index(request):

    return render(request,'index.html')


def home()

def employee(request):
    if request.method=="POST":
        name=request.POST.get('name')
        
        father_name=request.POST.get('father_name')
        hometown=request.POST.get('hometown')
        address=request.POST.get('address')
        dob=datetime()
        contact_no=request.POST.get('contact_no')
        Employee1=Employee1(name=name,father_name=father_name,hometown=hometown,address=address,
                           dob=datetime(),contact_no=contact_no)
        Employee1.save()
        
        
    
    
    return render(request,'employee.html')