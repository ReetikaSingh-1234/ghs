from django.shortcuts import render,HttpResponse
from .models import Employee1
from employee.models import Employee1

from django.shortcuts import render

def index_view(request):
    return render (request,'index.html')
def about_view(request):
    return render (request,'about.html')
def service_view(request):
    return render (request,'service.html')
def team_view(request):
        return render (request,'team.html')


def index(request):
    return HttpResponse("this is home page")
def about(request):
    return HttpResponse("this is about page")
def services(request):
    return HttpResponse("this is services page")
def contact(request):
    return HttpResponse("this is contact page")
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')
def show(request):
    return render(request,'show.html')
def team(request):
    return render(request,'team.html')
def services(request):
    return render(request,'about.html')
    
def employee(request):
    if request.method=="POST":
        obj=Employee1()
        obj.name=request.POST.get('name')
        
        obj.father_name=request.POST.get('father_name')
        obj.hometown=request.POST.get('hometown')
        obj.address=request.POST.get('address')
        
        obj.contact_no=request.POST.get('contact_no')
        
        obj.adhaarcard=request.POST.get('adhaarcard')
        
        
       
        if len(request.FILES)!=0:
                obj.adhaarcard=request.FILES['adhaarcard']
            
        obj.save()
        
        obj.pancard=request.POST.get('pancard')
        
        if len(request.FILES)!=0:
            obj.pancard=request.FILES['pancard']
            
        obj.save()
        
        obj.year1=request.POST.get('year1')
        obj.percentage1=request.POST.get('percentage1')
        obj.pdf1=request.POST.get('pdf1')
        
        if len(request.FILES)!=0:
            obj.pdf1=request.FILES['pdf1']
        obj.save()
        obj.year2=request.POST.get('year2')
        obj.percentage2=request.POST.get('percentage2')
        obj.pdf2=request.POST.get('pdf2')
        
        if len(request.FILES)!=0:
            obj.pdf2=request.FILES['pdf2']
        obj.save()
        obj.year3=request.POST.get('year3')
        obj.percentage3=request.POST.get('percentage3')
        obj.pdf3=request.POST.get('pdf3')
        
        if len(request.FILES)!=0:
            obj.pdf3=request.FILES['pdf3']
        obj.save()
        
        obj.year4=request.POST.get('year4')
        obj.percentage4=request.POST.get('percentage4')
        obj.pdf4=request.POST.get('pdf4')
        
        if len(request.FILES)!=0:
            obj.pdf4=request.FILES['pdf4']
        obj.save()
        
        
        obj.company_name=request.POST.get('company_name')
        obj.start=request.POST.get('start')
        obj.end=request.POST.get('end')
        obj.reason=request.POST.get('reason')
        obj.reference=request.POST.get('reference')
        obj.reference_no=request.POST.get('reference_no')
        obj.emailid=request.POST.get('emailid')
        
        obj.save()

        
    return render(request,'employee.html') 
def show(request):
    Employee2 = Employee1.objects.all
    return render(request, 'show.html',{'Employee2':Employee2})
