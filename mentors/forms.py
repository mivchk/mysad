from django import forms
from .models import Reminders, Attendance, Group
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import datetime as dt
from django.forms import formset_factory


class ReminderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = 'Сообщение'
        self.fields['deadline'].label = 'Срок напоминания'
    class Meta:
        model = Reminders
        fields = ['message', 'deadline']
        widgets = {
            'deadline': forms.SelectDateWidget(),
            'message': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['is_arrived']

AttendanceFormFormSet = formset_factory(AttendanceForm, extra=0)