from django import forms
from .models import UserData

class UserForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Jayvie"}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Ferrer"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "De Leon"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "4"}))
    course = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "BSIT"}))
    semester = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Second"}))

    class Meta:
        model = UserData
        fields = ['first_name', 'middle_name', 'last_name', 'gender', 'year', 'course', 'semester']
        labels = {
            'first_name': 'First Name', 
            'middle_name': 'Middle Name', 
            'last_name': 'Last Name', 
            'gender': 'Gender', 
            'year': 'Year',
            'course': 'Course',
            'semester': 'Semester',
        }