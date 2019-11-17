"""
Definition of models.
"""

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class client(models.Model):
    
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s '%(self.name, self.surname)

class labs(models.Model):
        
        def __str__(self):
            return '%s '%(self.lab)

class modules(models.Model):
    modul = models.CharField(max_length=50)
    def __str__(self):
        return '%s '%(self.modul)
    
class institution(models.Model):
    
    name = models.CharField(max_length=50)
    location = models.CharField(max_length = 250)
    type = models.CharField(max_length = 20)
    sub_name = models.CharField(max_length= 50)
    lab_1 = models.CharField(max_length=50)
    lab_2 = models.CharField(max_length=50)
    
    def __str__(self):
        return '%s %s %s %s %s %s'%(self.name, self.location, self.type, self.sub_name)
