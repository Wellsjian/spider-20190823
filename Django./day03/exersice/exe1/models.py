from django.db import models

# Create your models here.
class Xiaojian(models.Model):
    name = models.CharField("姓名",max_length=32,default="jian")
    age = models.IntegerField("年龄",default=25)
    time = models.DateField("出版日期",auto_now_add=True)