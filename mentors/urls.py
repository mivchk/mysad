from django.urls import path, include
from mentors.views import reminder_set, attendance_set, get_group, get_child, show_prepod, navbar

urlpatterns = [
    path('reminder/', reminder_set, name='reminder'),
    path('att/<int:child_id>/', attendance_set, name='attendance'),
    path('get_group/', get_group, name='get_group'),
    path('child_list/<int:group_number>/', get_child, name='get_child'),
    path('hello_prep/<prepod>/', show_prepod),
    path('navbar/', navbar),
]