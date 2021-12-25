from django import forms
from .models import Blogdetails




class addblog(forms.ModelForm):
    class Meta:
        model = Blogdetails
        fields = '__all__'

