from django.db import models

# Create your models here.

class Person(models.Model):
    GENDER = (
        ('M','Male'),
        ('F','Female')
    )
    name = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=1,choices=GENDER)
