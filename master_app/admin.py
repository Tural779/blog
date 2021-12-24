from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Blogvillage)
admin.site.register(models.Blogaccomodation)
admin.site.register(models.Blogtransportation)
admin.site.register(models.Blogname)
admin.site.register(models.Blogtext)