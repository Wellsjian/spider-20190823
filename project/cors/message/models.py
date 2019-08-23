from django.db import models
from user import models as u_models
from topic import models as t_models

# Create your models here.
class Message(models.Model):
    topic = models.ForeignKey(t_models.Topic)
    publisher = models.ForeignKey(u_models.UserProfile)
    content = models.CharField(verbose_name='内容',max_length=90)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    #父级Message_id  默认为0 表示留言   非0 表示  回复留言
    parent_message = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'message'
    
