from django.db import models

# Create your models here.


class Profile(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    objective = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    university = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    previous_work = models.CharField(max_length=200)




