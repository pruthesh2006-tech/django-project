from django.db import models

# Create your models here.

class Student(models.Model):
    sname = models.CharField(max_length=50, blank=False)
    smobile = models.CharField(max_length=10, blank=False)
    semail = models.EmailField(max_length=200)
    saddress = models.CharField(max_length=200)

    def __str__(self):
        return self.sname
    