from django.db import models

# Create your models here.
class SignUpDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    objective=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    pass1=models.CharField(max_length=150,null=True,blank=True)
    pass2=models.CharField(max_length=100,null=True,blank=True)
    weight=models.IntegerField(null=True,blank=True)
    height=models.IntegerField(null=True,blank=True)
    profile_image=models.ImageField(upload_to="profile",null=True,blank=True)

class CartDb(models.Model):
     name=models.CharField(max_length=100,null=True,blank=True)
     ProductImage=models.ImageField(upload_to="cart",null=True,blank=True)
     ProductName=models.CharField(max_length=100,null=True,blank=True)
     quantity=models.CharField(max_length=100,null=True,blank=True)
     Price=models.CharField(max_length=100,null=True,blank=True)
     total=models.CharField(max_length=100,null=True,blank=True)

class OrderDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Place=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100, null=True, blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    Address=models.CharField(max_length=100, null=True, blank=True)
    Total=models.IntegerField(null=True, blank=True)
    Messages=models.CharField(max_length=100,null=True,blank=True)

class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(max_length=100, null=True, blank=True)
    phone_no=models.IntegerField(null=True,blank=True)
    objective=models.CharField(max_length=100, null=True, blank=True)
    Message=models.CharField(max_length=200,null=True,blank=True)
