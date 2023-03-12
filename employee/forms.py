from django import forms 
#from django.core.exceptions import ValidationError
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'hire_date', 'hourly_rate']

        # Adding widgets to specify input types for each field
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'hire_date': forms.DateInput(attrs={'class': 'form-control' ,'type': 'date'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        # Adding custom validation to check if the email address is unique
        def clean_email(self):
            email = self.cleaned_data['email']
            existing_employee = Employee.objects.filter(email=email).exclude(id=self.instance.id).first()
            if existing_employee:
                raise forms.ValidationError('Thisemail address is already in use.')
            return email