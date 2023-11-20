from django.db import models

class Kids(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
