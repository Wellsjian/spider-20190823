from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField("姓名", max_length=30)

    def __str__(self):
        return "作者:" + self.name


class Book(models.Model):
    title = models.CharField("书名", max_length=50)
    # Book中添加authors属性来绑定Author表
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return "书名:" + self.title
