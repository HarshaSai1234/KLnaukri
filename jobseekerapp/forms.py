from django import forms
from .models import *
class jobseekerprofileform(forms.ModelForm):
    class Meta:
        model = jobseekerprofile
        fields = ['name', 'qualification','hobbies','skills','address','profile_photo']