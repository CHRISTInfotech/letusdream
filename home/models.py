from django.db import models
# from django_countries.fields import CountryField

# Create your models here.
class ConferenceRegistration(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20,null=True)
    email=models.CharField(max_length=20)
    interest=models.CharField(max_length=20)
    user_type=models.CharField(max_length=50)
    st_addr=models.CharField(max_length=50,null=True)
    # st_phone=models.CharField(max_length=50,null=True)
    st_grade=models.CharField(max_length=50,null=True)
    st_Pname=models.CharField(max_length=50,null=True)
    st_Pnum=models.CharField(max_length=50,null=True)
    st_Pemail=models.CharField(max_length=50,null=True)
    st_Paddr=models.CharField(max_length=50,null=True)
    vl_type=models.CharField(max_length=50,null=True)
    vl_about=models.CharField(max_length=50,null=True)
    vl_expert=models.CharField(max_length=50,null=True)
    ptr_addr=models.CharField(max_length=50,null=True)
    ptr_msg=models.CharField(max_length=50,null=True)
    # date = models.DateField(auto_now_add = True)   
    date = models.DateField(("DDMMYY"), auto_now_add=True)


# class Visitor(models.Model):
#     country = CountryField()
#     code = CountryField()
#     count = models.IntegerField()

