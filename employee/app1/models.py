from django.db import models

# Create your models here.

class employee(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="media/",null=True,blank=True)