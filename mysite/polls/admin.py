
from django.contrib import admin
from .models import Question, Choice

# Register your models here.
admin.site.register(Question)  #Question オブジェクトがadmin インタフェースを持つということを、adminに伝える
admin.site.register(Choice)
