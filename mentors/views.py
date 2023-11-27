from django.shortcuts import render
from .forms import ReminderForm


def reminder_set(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReminderForm()
    return render(request, 'forms_mentors.html', {'form': form})