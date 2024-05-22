from django.db import models

# Create your models here.

class Technologies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Nombre:{self.name}"

class Project(models.Model):

    name = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=200, blank=False, default="")
    technologies = models.ManyToManyField(Technologies, related_name='Projects')
    image = models.ImageField(upload_to='images/')

 