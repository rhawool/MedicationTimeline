from django.forms import ModelForm
from datetime import datetime
from timeline_app.models import IntakeEntry
from django import forms


class AddEntryForm(ModelForm):
    class Meta:
        model = IntakeEntry
        fields = ['medicine_name']


class UpdateEntryDataForm(ModelForm):
    class Meta:
        model = IntakeEntry
        MEDICINE_CHOICES = [
            ('Ebast-20', 'Ebast-20'),
            ('Levocitrizine', 'Levocitrizine'),
        ]
        widgets = {
            'medicine_name': forms.Select(choices=MEDICINE_CHOICES, attrs={'class': 'form-control'}),
        }
        fields = ['intake_time', 'medicine_name']
