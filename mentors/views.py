from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import ReminderForm, AttendanceForm, GroupForm
from .models import Child, Attendance, Group
import datetime as dt
from django.contrib.auth.decorators import login_required


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

    children = Child.objects.filter(group_id_id=group_number)
    today = str(dt.date.today())
    dates = [str(i) for i in Attendance.objects.filter(group_id=group_number).values_list('today_date', flat=True).distinct()]
    for child in children:
        if today in dates:
            continue
        else:
            Attendance.objects.create(
                child_id=child.child_id,
                group_id=group_number,
                child_name=child.child_name
            )

    children = Attendance.objects.filter(group_id=group_number, today_date=today)
    if request.method == 'POST':
        for child in children:
            is_arrived = request.POST.get(str(child.attendance_id), False)
            child.is_arrived = is_arrived == 'on'
            child.save()

    return render(request, 'mentors/mark_attendance_temp.html', {'children': children})


# На этой вьюшке ты выбираешь группу, по которой будешь выставлять посещаемость
@login_required
def get_group_view(request):
    group = Group.objects.values_list('group_id', flat=True)
    return render(request, 'mentors/get_group_temp.html', {'group': group})
