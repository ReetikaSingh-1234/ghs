from django.db import models
import os





# Create your models here.
class Employee1(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    father_name=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    hometown=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    address=models.CharField(max_length=50,null=False,blank=False,default='unknown')
   
    contact_no=models.CharField(max_length=50,null=False,blank=True,default='unknown')
    adhaarcard=models.ImageField(upload_to="images/Employee2",default='unknown')
    pancard=models.ImageField(upload_to="images/Employee2",default='unknown')
    year1=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    percentage1=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    pdf1=models.FileField(upload_to="images/Employee2",default='unknown')
    year2=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    percentage2=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    pdf2=models.FileField(upload_to="images/Employee2",default='unknown')
    year3=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    percentage3=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    pdf3=models.FileField(upload_to="images/Employee2",default='unknown')
    year4=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    percentage4=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    pdf4=models.FileField(upload_to="images/Employee2",default='unknown')
    company_name=models.CharField(max_length=50,default='unknown')
    start=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    end=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    reason=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    reference=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    reference_no=models.CharField(max_length=50,null=False,blank=False,default='unknown')
    
    emailid=models.CharField(max_length=50,default='unknown')
    def __str__(self):
        return self.name
        