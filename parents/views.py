from django.shortcuts import render
from .models import Schedule, Family
from datetime import datetime as dt
import pytz
from mentors.models import Reminders
from django.contrib.auth.decorators import login_required

mtz = pytz.timezone('Europe/Moscow')
now = dt.now(mtz)


@login_required
def main_view(request):
    schedule = Schedule.objects.filter(start__lt=now, end__gt=now).first()
    reminder = Reminders.objects.order_by('-deadline').first()
    family_surname = Family.objects.filter(family_id=1).first()
    return render(request, 'parents/main_temp.html', {'schedule': schedule, 'reminder': reminder, 'surname': family_surname})
