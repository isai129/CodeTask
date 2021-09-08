from django.db import models


# Create your models here.

class UserInfo(models.Model):  # 要继承这个类（固定写法）。
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    # 创建两个字段，最大长度32，类型是char
