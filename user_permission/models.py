from django.db import models

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=20)
    users = models.ManyToManyField('auth.User', blank=True, db_constraint=False)