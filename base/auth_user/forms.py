from django import forms
from .models import UserData

class UserForm(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['fname', 'mname', 'lname', 'year', 'course', 'semester']
        labels = {
            #'student_number': 'Student Number', 
            'fname': 'First Name', 
            'mname': 'Middle Name', 
            'lname': 'Last Name', 
            'year': 'Year',
            'course': 'Course',
            'semester': 'Semester',
        } 
        widgets = {
            #'student_number': forms.TextInput(attrs={'class': 'form-control'}), 
            'fname': forms.TextInput(attrs={'class': 'form-control'}), 
            'mname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}), 
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}), 
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
        }