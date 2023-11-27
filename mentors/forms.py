from django import forms
from .models import Reminders
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import datetime as dt


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminders
        fields = ['message', 'deadline']
        widgets = {
            'deadline': DatePickerInput()
        }