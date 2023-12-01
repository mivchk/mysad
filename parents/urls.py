from django.urls import path, include
from parents.views import schedule_view

urlpatterns = [
    path('schedule/', schedule_view, name='schedule'),
]