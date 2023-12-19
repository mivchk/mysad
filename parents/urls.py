from django.urls import path, include
from parents.views import schedule_view, reminder_view

urlpatterns = [
    path('schedule/', schedule_view, name='schedule'),
    path('reminder/', reminder_view, name='p_reminder')
]