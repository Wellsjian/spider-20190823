from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("书名",max_length=50,null=True,default="")
    pub_host = models.CharField("出版社",max_length=50,null=True,default="清华大学出版社")
    pub_time = models.DateField('出版时间',default='2017-12-12')
    price = models.DecimalField("价格",max_digits=7,decimal_places=2,default=0.0)

    def __str__(self):
        return "书名:" + self.title + "出版社" + self.pub_host
class Author(models.Model):
    name = models.CharField("作者",max_length=20,unique=True,db_index=True)
    age = models.IntegerField("年龄",default=1)
    emill = models.EmailField("邮箱",null=True)