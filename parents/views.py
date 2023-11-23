from django.shortcuts import render
from .models import Schedule
from datetime import datetime as dt
import pytz

mtz = pytz.timezone('Europe/Moscow')
now = dt.now(mtz)


def schedule_view(request):
    schedule_data = Schedule.objects.filter(start__lt=now, end__gt=now).first()
    return render(request, 'schedule_template.html', {'schedule_data': schedule_data})
