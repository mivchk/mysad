from datetime import datetime
from django.db import models


class Mentor(models.Model):
    mentor_id = models.AutoField(primary_key=True)
    mentor_name = models.CharField(max_length=100)
    professional_grade = models.CharField(max_length=100)
    username = models.CharField(max_length=20, default=models.SET_NULL, null=True)
    password = models.CharField(max_length=20, default=models.SET_NULL, null=True)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    mentor_id = models.ForeignKey('Mentor', on_delete=models.CASCADE)
    grade = models.IntegerField()


class Reminders(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=255)
    deadline = models.DateField()


class Attendance(models.Model):
    attendance_id = models.AutoField(primary_key=True)
    today_date = models.DateField(default=datetime.today)
    child = models.ForeignKey('Child', on_delete=models.CASCADE)
    is_arrived = models.BooleanField(default=False)
    group = models.ForeignKey('Group', on_delete=models.CASCADE, null=True)
    child_name = models.CharField(max_length=100, null=True)


class Child(models.Model):
    child_id = models.AutoField(primary_key=True)
    child_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    group_id = models.ForeignKey('Group', on_delete=models.CASCADE)



