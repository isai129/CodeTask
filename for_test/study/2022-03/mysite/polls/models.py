from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone


#  import datetime 和 from django.utils import timezone
#  分别导入了 Python 的标准 datetime 模块和 Django 中和时区相关的 django.utils.timezone 工具模块

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 每个 Choice 对象都关联到一个 Question 对象
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # 将votes的默认值，设为0。

    def __str__(self):
        return self.choice_text



