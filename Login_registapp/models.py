from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20,)
    gender = models.CharField(max_length=10)


class Staff(models.Model):
    Headpic = models.ImageField(upload_to='picspy', null=True)  # 上传的头像保存在picspy
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    # Gender = models.CharField(max_length=10)
    Birthday = models.DateField(null=True)
    Salary = models.FloatField(null=True)
