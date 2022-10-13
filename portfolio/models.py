from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.db.models.fields.files import ImageField


class Project(models.Model):
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)