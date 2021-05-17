from django.db import models

# Create your models here.
class doc(models.Model):
    name1=models.CharField(max_length=50)
    name2=models.CharField(max_length=50)
    result=models.CharField(max_length=50)