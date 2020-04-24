from django.db import models

# Create your models here.
class Post(models.Model):
    postid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    enrollmentnumber=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    description = models.CharField(max_length=10000)
    status = models.IntegerField()
    dt = models.CharField(max_length=100)
