from django.db import models

# Create your models here.
class ConferenceRegistration(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    aboutme=models.CharField(max_length=20)
    aboutother=models.CharField(max_length=100,null=True)
    orgaff=models.CharField(max_length=50)
    orgname=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,null=True)
    confdate=models.CharField(max_length=50)
    prevconf=models.CharField(max_length=50)

