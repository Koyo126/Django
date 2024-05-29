
from django.contrib import admin
from .models import Question, Choice

# Register your models here.
#class QuestionAdmin(admin.ModelAdmin):
##    fields = ["pub_date", "question_text"]
#    # fieldsets の各タプルの先頭の要素はフィールドセットのタイトル
#    fieldsets = [
#        #(None, {"fields": ["question_text"]}),
#        ("TEST", {"fields": ["question_text"]}),
#        ("Date information", {"fields": ["pub_date"]}),
#    ]

#admin.site.register(Question)  #Question オブジェクトがadmin インタフェースを持つということを、adminに伝える

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline): # TabularInline を使うと、 リレーション相手のオブジェクトはコンパクトなテーブル形式で表示される
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        # "classes": ["collapse"] --- 隠すことができるようになる
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
        #("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    # 「フィルタ (Filter)」サイドバーができ、チェンジリストを pub_date フィールドの値に従ってフィルタできるようになる
    list_filter = ["pub_date"]

    # チェンジリストの上部に検索ボックスが表示される
    search_fields = ["question_text"]

# モデルの admin のオプションを変更したいときには、モデルごとに admin クラスを作成して、 
# admin.site.register() の 2 番目の引数に渡す
admin.site.register(Question, QuestionAdmin)

#admin.site.register(Choice)
