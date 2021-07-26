from django import forms
from .models import Apartment

class ApartmentForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    street_address = forms.CharField(label='Street Address', max_length=100)
    apartment_img = forms.ImageField(label='Select Image', max_length=100)
    monthly_rent = forms.DecimalField(label='Monthly Rent')
    renovated = forms.BooleanField(required=False)
    air_conditioning = forms.BooleanField(required=False)
    pool = forms.BooleanField(required=False)
    allows_pets = forms.BooleanField(required=False)
    laundry_onsite = forms.BooleanField(required=False)
    contact_number = forms.CharField(required=False, max_length=12)



