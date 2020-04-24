from django.db import models

class Register(models.Model):
    regid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    enrollmentnumber=models.CharField(max_length=50)
    college = models.CharField(max_length=20)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    gender = models.CharField(max_length=13)
    status = models.IntegerField()
    role = models.CharField(max_length=50)
    dt = models.CharField(max_length=100)
