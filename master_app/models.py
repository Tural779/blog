from django.db import models
from django.contrib import admin


# Create your models here.
## https://docs.djangoproject.com/en/3.2/topics/db/models/



class Blogdetails(models.Model):
   villages = models.CharField(max_length=55)
   accomodations = models.CharField(max_length=255)
   transportations = models.CharField(max_length=255)
   text = models.CharField(max_length=5000)




























