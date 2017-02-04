# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from djng.views.crud import NgCRUDView
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.创建数据表结构
class Person(models.Model):
    name = models.CharField(max_length=30)
    password = models.IntegerField()
    email=models.CharField(max_length=30)


    def __unicode__(self):
        # 在Python3中使用 def __str__(self)
        return self.name


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    name = models.CharField(max_length=30)
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title

