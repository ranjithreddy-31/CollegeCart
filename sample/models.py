from django.db import models

# Create your models here.
class project(models.Model):
    uname=models.CharField(max_length=20,null=True)
    name=models.CharField(max_length=20)
    i=models.ImageField(upload_to='media',blank=True, null=True)
    email=models.EmailField(max_length=254,null=True)
    phone=models.CharField(max_length=10,null=True)
    Name_of_Product=models.CharField(max_length=50,null=True)
    description=models.TextField(null=True)
    u_id=models.IntegerField(null=True)


class Register(models.Model):
    Name=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
