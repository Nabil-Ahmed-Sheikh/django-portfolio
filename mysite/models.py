from django.db import models

# Create your models here.

class Testimony(models.Model):
    person_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/testimony')
    testimony = models.TextField()
    show = models.BooleanField(default=False)

class Technology(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to = 'images/technolohy')
    show = models.BooleanField(default=False)