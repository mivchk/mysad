from django import forms
from .models import Reminders, Attendance, Group
from bootstrap_datepicker_plus.widgets import DatePickerInput
from datetime import datetime as dt


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminders
        fields = ['message', 'deadline']
        widgets = {
            'deadline': forms.SelectDateWidget(),
            'message': forms.TextInput(),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['is_arrived']


class GroupForm(forms.Form):
    group = forms.ModelChoiceField(queryset=Group.objects.values_list('group_id', flat=True), empty_label=None)