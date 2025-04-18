from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    country = models.CharField(max_length=30)
    programming_language = models.CharField(max_length=40)


    def __str__(self):
        return self.name

