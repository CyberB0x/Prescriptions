from django import forms
from .models import Prescription

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['doctor_name', 'patient_name', 'patient_email', 'content']
