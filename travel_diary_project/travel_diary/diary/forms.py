
from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['title', 'description', 'location', 'image', 'cost', 'heritage_sites', 'visitable_places', 'rating', 'latitude', 'longitude']
