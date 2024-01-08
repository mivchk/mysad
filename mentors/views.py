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

    print(today)
    print(dates)
    return render(request, 'mentors/mark_attendance_temp.html', {'children': children})


# На этой вьюшке ты выбираешь группу, по которой будешь выставлять посещаемость
@login_required
def get_group_view(request):
    # if request.method == 'POST':
    #     group_number = request.POST.get('group_number')
    #     return redirect('child', group_number=group_number)
    group = Group.objects.values_list('group_id', flat=True)
    return render(request, 'mentors/get_group_temp.html', {'group': group})


# Этот метод еще не до конца реализован, по идее копирует детей в посещаемость со сегодняшней датой
# # TODO: создать триггер для этого метода (Надо чтобы срабатывал когда препод заходит в посещаемость либо ночью) 
# def copy_children_to_attendance(request):
#     children = Child.objects.all()
#     for child in children:
#         Attendance.objects.create(
#                 child_id=child.child_id,
#                 mentor_id=1,
#                 child_name=child.child_name
#             )

#     return HttpResponse("Дети успешно скопированы в таблицу посещаемости.")



# def get_child(request, group_number):
#     children = Child.objects.filter(group_id_id=group_number)
#     for child in children:
#         if child.child_id in Attendance.objects.values_list('child_id', flat=True):
#             continue
#         else:
#             Attendance.objects.create(
#                 child_id=child.child_id,
#                 group_id=group_number,
#                 child_name=child.child_name
#             )
#     att = Attendance.objects.all()
#     return render(request, 'show_kids.html', {'children': att})


# def show_prepod(request, prepod):
#     return HttpResponse(f'Привет, {prepod}')


# def navbar(request):
#     return render(request, 'bebra.html')


# def attendance_set(request, child_id):
#     child = get_object_or_404(Attendance, pk=child_id)
#     if request.method == 'POST':
#         form = AttendanceForm(request.POST, instance=child)
#         if form.is_valid():
#             form.save()
#     else:
#         form = AttendanceForm(instance=child)
#     return render(request, 'attendance_form.html', {'form': form, 'name': child.child_name, 'check': child.is_arrived})
    

# def get_group(request):
#     groups = Group.objects.values_list('group_id')
#     return render(request, 'group_list.html', {'list': groups[0]})