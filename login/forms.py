from django import forms
from django.core import validators
from django.db import models
from webcam.fields import CameraField

class Person(models.Model):
    picture = CameraField()
    
    