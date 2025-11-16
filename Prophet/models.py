from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Learner(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    roll = models.IntegerField()
    
    def __str__(self):
        return self.name