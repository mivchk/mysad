from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import ReminderForm, AttendanceFormFormSet
from .models import *
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def main_view(request):
    return render(request, 'mentors/main_page.html')


# Эта вьюшка для создания напоминаний воспитателями
@login_required
def reminder_view(request): 
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReminderForm()
    return render(request, 'mentors/m_reminder_temp.html', {'form': form})


# На эту вьюшку перекидывает, чтобы проставить посещаемость с вьюшки "get_group"
@login_required
def mark_attendance_view(request, group_number):
    today = dt.date.today()
    children = Child.objects.filter(group_id_id=group_number)
    
    attendance_exists = Attendance.objects.filter(group_id=group_number, today_date=today).exists()
    if not attendance_exists:
        for child in children:
            Attendance.objects.create(
                child_id=child.child_id,
                group_id=group_number,
                child_name=child.child_name,
                today_date=today
            )

    children2 = Attendance.objects.filter(group_id=group_number, today_date=today)
    if request.method == 'POST':
        for child in children2:
            is_arrived = request.POST.get(str(child.attendance_id))
            child.is_arrived = is_arrived == 'on'
            child.save()

    return render(request, 'mentors/mark_attendance_temp.html', {'children': children2})



# На этой вьюшке ты выбираешь группу, по которой будешь выставлять посещаемость
@login_required
def get_group_view(request):
    group = Group.objects.values_list('group_id', flat=True)
    if request.method == 'POST':
        group_number = request.POST.get('group_number')
        return redirect(reverse('get_child', kwargs={'group_number': group_number}))
    return render(request, 'mentors/get_group_temp.html', {'group': group})
