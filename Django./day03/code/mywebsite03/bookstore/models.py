from django.db import models
import django.utils.timezone as timezone

# Create your models here.

#file : mywebsite03/bookstore/model.py
class Book(models.Model):
    title = models.CharField('书名',max_length=50)
    pub_host = models.CharField('出版社',max_length=50)
    price = models.DecimalField("定价", max_digits=7,decimal_places=2, default=0.0)
    date_add = models.DateTimeField("开始日期",default=timezone.now)
    put_date = models.DateField("出版时间",default='2017-1-1')#auto_now =True,auto_now_add = True







