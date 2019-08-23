from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField("书名",max_length=50,default="",unique=True)
    price = models.DecimalField("价格",max_digits=7,decimal_places=2)
    pub_house = models.CharField("出版社",max_length=100,default="清华大学出版社")
    market_price = models.DecimalField("零售价",max_digits=7,decimal_places=2,default=9999)
    # def __str__(self):
    #     return   "书名:" + self.title + "出版社:" + self.pub_house
    # 内外函数  可以改动表名
    # class Meta:
    #     db_table = 'my_bookstore_book'

class Author(models.Model):
    name = models.CharField("名字",max_length=50)
    age = models.IntegerField('年龄',default=0)
    emill= models.EmailField("邮箱",default='wangfj@163.com')



class Wife(models.Model):
    name = models.CharField("姓名",max_length=50)
    author = models.OneToOneField(Author)