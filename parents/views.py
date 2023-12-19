from django.shortcuts import render
from .models import Schedule
from datetime import datetime as dt
import pytz
from mentors.models import Reminders

mtz = pytz.timezone('Europe/Moscow')
now = dt.now(mtz)


def schedule_view(request):
    schedule_data = Schedule.objects.filter(start__lt=now, end__gt=now).first()
    return render(request, 'parents/schedule_temp.html', {'schedule_data': schedule_data})


def reminder_view(request):
    reminder_data = Reminders.objects.order_by('-deadline').first()
    return render(request, 'parents/p_reminder_temp.html', {'reminder': reminder_data})

