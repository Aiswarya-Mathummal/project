from django.db import models

# Create your models here.

class user_register(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    photo=models.ImageField(upload_to="media/",null=True,blank=True)
    
    
    def __str__(self):
        return self.username
    
class Galleryy(models.Model):
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to="media/",null=True,blank=True)
    description=models.CharField(max_length=70)
    price=models.IntegerField()
    
    def __str__(self) :
        return self.name