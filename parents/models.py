from django.db import models


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    start = models.TimeField()
    end = models.TimeField()
    grade = models.IntegerField(default=1)


class Family(models.Model):
    family_id = models.AutoField(primary_key=True)
    child_surname = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



