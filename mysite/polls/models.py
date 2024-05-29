import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")  #オプションとして人間可読なフィールド名も指定できます
    def __str__(self):
        return self.question_text

    # was_published_recently のカラムヘッダは、デフォルトではメソッド名 (アンダースコアを空白に置き換えたもの) になっている
    # 各行は戻り値の文字列表現
    # 以下で改善される

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
