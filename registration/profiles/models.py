from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Division(models.Model):
        name = models.CharField(max_length = 50)

        def __str__(self):
            return self.name

class District(models.Model):
        name = models.CharField(max_length = 50)
        division = models.ForeignKey(Division)

        def __str__(self):
            return self.name

class Area(models.Model):
    name = models.CharField(max_length = 50)
    district = models.ForeignKey(District)

    def __str__(self):
        return self.name

class Profile(models.Model):
    email = models.EmailField()
    phone = models.IntegerField()
    name = models.CharField(max_length = 50)
    area = models.ForeignKey(Area)
    user = models.OneToOneField(User)
    #photo = models.FileField()

    def __str__(self):
        return self.name
