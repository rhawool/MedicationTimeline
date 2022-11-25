from django.forms import ModelForm
from datetime import datetime
from timeline_app.models import IntakeEntry


#
# class AddMedicineForm(ModelForm):
#     class Meta:
#         model = Medicine
#         fields = '__all__'
#
class AddEntryForm(ModelForm):
    class Meta:
        model = IntakeEntry
        fields = ['medicine_name']
