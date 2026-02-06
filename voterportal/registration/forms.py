from django import forms
from .models import Voter

class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = ['first_name', 'last_name', 'gender', 'address', 'city', 'state', 'pincode', 'date_of_birth', 'contact']
        widgets = {
            'voter_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Voter ID'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter State'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pincode'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
        }
        labels = {
            'voter_id': 'Voter ID',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'gender': 'Gender',
            'address': 'Address',
            'city': 'City',
            'state': 'State',
            'pincode': 'Pincode',
            'date_of_birth': 'Date of Birth',
            'contact': 'Contact Number',
        }