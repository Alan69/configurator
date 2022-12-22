from django import forms  
from .models import Region, Urls

class RegionForm(forms.ModelForm):  
    class Meta:  
        model = Region  
        fields = ['url'] 
