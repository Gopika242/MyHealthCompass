from django.db import models
from .validators import file_size


# Create your models here.

class ShopCategoryDb(models.Model):
  CategoryName=models.CharField(max_length=100,null=True,blank=True)
  CategoryImage=models.ImageField(upload_to="CategoryImages",null=True,blank=True)
  Description=models.TextField(max_length=200,null=True,blank=True)

class ShopProductDb(models.Model):
  Category=models.CharField(max_length=100,null=True,blank=True)
  ProductName=models.CharField(max_length=100,null=True,blank=True)
  ProductImage=models.ImageField(upload_to="CategoryImages",null=True,blank=True)
  ProductDescription=models.TextField(max_length=200,null=True,blank=True)
  Price=models.IntegerField(null=True,blank=True)


class MealPlansDb(models.Model):
  Objective=models.CharField(max_length=100,null=True,blank=True)
  Diet=models.CharField(max_length=100,null=True,blank=True)
  Plan=models.CharField(max_length=100,null=True,blank=True)
  BreakFast=models.CharField(max_length=100,null=True,blank=True)
  BCalorie=models.IntegerField(null=True,blank=True)
  BImage=models.ImageField(upload_to="MealsImages",null=True,blank=True)
  Lunch=models.CharField(max_length=100,null=True,blank=True)
  LCalorie=models.IntegerField(null=True,blank=True)
  LImage=models.ImageField(upload_to="MealsImages",null=True,blank=True)
  Dinner=models.CharField(max_length=100,null=True,blank=True)
  DCalorie=models.IntegerField(null=True,blank=True)
  DImage=models.ImageField(upload_to="MealsImages",null=True,blank=True)

class videoDb(models.Model):
  Objective1=models.CharField(max_length=100, null=True, blank=True)
  caption=models.CharField(max_length=100,null=True,blank=True)
  video=models.FileField(upload_to="video/%y")
  calorie=models.CharField(max_length=100,null=True,blank=True)
  EDescription = models.TextField(max_length=200, null=True, blank=True)

class WorkoutPlansDb(models.Model):
  Title=models.CharField(max_length=100, null=True, blank=True)
  FObjective=models.CharField(max_length=100, null=True, blank=True)
  Monday=models.TextField(max_length=1000, null=True, blank=True)
  Tuesday=models.TextField(max_length=1000, null=True, blank=True)
  Wednesday=models.TextField(max_length=1000, null=True, blank=True)
  Thursday=models.TextField(max_length=1000, null=True, blank=True)
  Friday=models.TextField(max_length=1000, null=True, blank=True)
  Saturday=models.TextField(max_length=1000, null=True, blank=True)
  Sunday=models.TextField(max_length=1000, null=True, blank=True)

class BlogDb(models.Model):
  PublishDate=models.DateField()
  Heading=models.CharField(max_length=100, null=True, blank=True)
  BlogDescription=models.CharField(max_length=100, null=True, blank=True)
  intro=models.CharField(max_length=100, null=True, blank=True)
  Cover=models.ImageField(upload_to="BlogCovers",null=True,blank=True)
