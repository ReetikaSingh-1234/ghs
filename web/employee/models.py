from django.db import models
import os





# Create your models here.
class Employee1(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    father_name=models.CharField(max_length=50,null=False,blank=False)
    hometown=models.CharField(max_length=50,null=False,blank=False)
    address=models.CharField(max_length=50,null=False,blank=False)
   
    contact_no=models.CharField(max_length=50,null=False,blank=True)
    adhaarcard=models.ImageField(upload_to="images/Employee2")
    pancard=models.ImageField(upload_to="images/Employee2")
    year1=models.CharField(max_length=50,null=False,blank=False)
    percentage1=models.CharField(max_length=50,null=False,blank=False)
    pdf1=models.FileField(upload_to="images/Employee2")
    year2=models.CharField(max_length=50,null=False,blank=False)
    percentage2=models.CharField(max_length=50,null=False,blank=False)
    pdf2=models.FileField(upload_to="images/Employee2")
    year3=models.CharField(max_length=50,null=False,blank=False)
    percentage3=models.CharField(max_length=50,null=False,blank=False)
    pdf3=models.FileField(upload_to="images/Employee2")
    year4=models.CharField(max_length=50,null=False,blank=False)
    percentage4=models.CharField(max_length=50,null=False,blank=False)
    pdf4=models.FileField(upload_to="images/Employee2")
    company_name=models.CharField(max_length=50,null=False,blank=False)
    start=models.CharField(max_length=50,null=False,blank=False)
    end=models.CharField(max_length=50,null=False,blank=False)
    reason=models.CharField(max_length=50,null=False,blank=False)
    reference=models.CharField(max_length=50,null=False,blank=False)
    reference_no=models.CharField(max_length=50,null=False,blank=False)
    
    emailid=models.CharField(max_length=50,null=False,blank=False)
    def __str__(self):
        return self.name
        