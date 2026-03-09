from django import forms
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = useraccount
        fields = ['fname', 'lname', 'email', 'pnumber', 'role']