from django.db import models


# Create your models here.

class Users(models.Model):
    uname = models.CharField('姓名', max_length=30)
    upwd = models.CharField('密码', max_length=100)
    uemail = models.EmailField('电子邮箱')
    nickname = models.CharField('昵称',max_length=50)

    def __str__(self):
        return "姓名:" + self.uname
