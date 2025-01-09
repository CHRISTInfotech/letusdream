from unittest.util import _MAX_LENGTH
from django.db import models


class LUDPrograms(models.Model):
    title = models.CharField(max_length=255)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.__str__()

# Create your models here.
class SubscribeNewsletter(models.Model):
    email = models.EmailField(null=False,blank=False)
    program = models.ForeignKey(LUDPrograms,on_delete=models.CASCADE)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email.__str__()