from django.db import models
from django.contrib import admin


# Create your models here.
## https://docs.djangoproject.com/en/3.2/topics/db/models/



class Blogname(models.Model):
   name= models.CharField(max_length=55)

class Blogvillage(models.Model):
    villages = models.CharField(max_length=255)

class Blogaccomodation(models.Model):
    accomodations = models.CharField(max_length=255)

class Blogtransportation(models.Model):
    transportations = models.CharField(max_length=255)

class Blogtext(models.Model):
    text = models.CharField(max_length=5000)



























