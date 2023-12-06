from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .forms import ReminderForm, AttendanceForm, GroupForm
from .models import Child, Attendance, Group


def reminder_set(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReminderForm()
    return render(request, 'forms_mentors.html', {'form': form})


def attendance_set(request, child_id):
    child = get_object_or_404(Attendance, pk=child_id)
    child_name = child.child_name
    check = child.is_arrived
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=child)
        if form.is_valid():
            form.save()
    else:
        form = AttendanceForm(instance=child)
    return render(request, 'attendance_form.html', {'form': form, 'name': child_name, 'check': check})
    

# def get_group(request):
    groups = Group.objects.values_list('group_id')
    return render(request, 'group_list.html', {'list': groups[0]})


def get_group(request):
    if request.method == 'POST':
        group_number = request.POST.get('group_number')
        return redirect('get_child', group_number=group_number)
    group = Group.objects.values_list('group_id', flat=True)
    return render(request, 'group_list.html', {'group': group})



def get_child(request, group_number):
    children = Child.objects.filter(group_id_id=group_number).values_list('child_name', flat=True)
    return render(request, 'show_kids.html', {'children': children})


def show_prepod(request, prepod):
    return HttpResponse(f'Привет, {prepod}')


def navbar(request):
    return render(request, 'bebra.html')
