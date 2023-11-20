from django.db import models


class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    start = models.TimeField()
    end = models.TimeField()