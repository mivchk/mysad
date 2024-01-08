from django.urls import path, include
from mentors.views import reminder_view, get_group_view, mark_attendance_view

urlpatterns = [
    path('reminder/', reminder_view, name='m_reminder'),
    path('get_group/', get_group_view, name='get_group'),
    path('child_list/<int:group_number>/', mark_attendance_view, name='get_child'),
    # path('att/<int:child_id>/', attendance_set, name='attendance'),
    # path('child_list/<int:group_number>/', get_child, name='get_child'),
    # path('hello_prep/<prepod>/', show_prepod),
    # path('navbar/', navbar),
]