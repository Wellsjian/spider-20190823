from django.db import models


# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(verbose_name='用戶名', max_length=11, primary_key=True)
    nickname = models.CharField(verbose_name='昵称', max_length=30)
    email = models.EmailField(verbose_name='邮箱', max_length=50)
    password = models.CharField(verbose_name='密码', max_length=64)
    sign = models.CharField(verbose_name='个人签名', max_length=50, null=True)
    info = models.CharField(verbose_name='个人描述', max_length=150, null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True)
    score = models.IntegerField(verbose_name='分数', null=True, default=0)

    def __str__(self):
        return "用户名" + self.username

    # 自定义表名
    class Meta:
        db_table = 'user_profile'
