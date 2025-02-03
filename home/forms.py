from .models import Contact
from django import forms



class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ['user']
        labels = {
            'body': 'Message', 'phnNum':'Phone Number'
        }

