from django import forms
from .models import Employee1


class HotelForm(forms.ModelForm):

    class Meta:
        model = Employee1
        fields = ['name', 'father_name','hometown','address','contact_no','adhaarcard']