from django import forms
from .models import Post,Profile, Business,Neighbourhood

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'location', 'occupant_id']
        
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ['name','post','post_caption','neighbourhood']
        
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model= Business
        fields = ['name','b_email','image']    
        
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model= Neighbourhood
        fields = ['neighbourhood_name','neighbourhood_location','occupants_count']              