from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField("用户名",max_length=20)
    password = models.CharField('密码',max_length=50)
    def __str__(self):
        return "用户名" + self.username

class Note(models.Model):
    title = models.CharField("名字",max_length=30)
    content = models.TextField("内容")
    create_time = models.DateField("创建时间",auto_now_add=True)
    mod_time = models.DateField("修改时间",auto_now=True)
    users = models.ForeignKey(User)
    def __str__(self):
        return "名字" + self.title
