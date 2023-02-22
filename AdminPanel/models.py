from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class Registration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=50)
    dreams=models.CharField(max_length=20)
    dreamsOption=models.CharField(max_length=20)



# class DreamsEvent(models.Model):
#     events=models.CharField(max_length=20)

# class DreamsOption(models.Model):
#     options=models.CharField(max_length=20)
#     events=models.ForeignKey(DreamsEvent,ondelete=models.CASCADE)

    