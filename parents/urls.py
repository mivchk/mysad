from django.urls import path
from parents.views import main_view

urlpatterns = [
    path('', main_view, name='main'),
    ]