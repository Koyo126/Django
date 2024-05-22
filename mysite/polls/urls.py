#ビューを呼ぶために、 URL を対応付けしてやる

from django.urls import path

from . import views

app_name = "polls"  #名前空間の追加
urlpatterns = [
    path("", views.index, name="index"), # http://127.0.0.1:8000/polls/
    
    path("<int:question_id>/", views.detail, name="detail"), # /polls/34/ -> detail(request=<HttpRequest object>, question_id=34)
    
    path("<int:question_id>/results/", views.results, name="results"), # /polls/5/results/

    path("<int:question_id>/vote/", views.vote, name="vote"), # /polls/5/vote/
]

