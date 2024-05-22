from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # polls/index.html(polls/templates/polls/index.html) というテンプレートをロードし、そこにコンテキストを渡します
    #template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    #output = ", ".join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return HttpResponse(template.render(context, request))

    #テンプレートをロードしてコンテキストに値を入れ、テンプレートをレンダリングした結果を HttpResponse オブジェクトで返す
    # render() 関数の引数
    # (1) request オブジェクト (2) テンプレート名 (3) 辞書（任意）
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    ## リクエストした ID を持つ質問が存在しないときに Http404 を送出
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, "polls/detail.html", {"question": question})  # polls/templates/polls/detail.html
    
    #return HttpResponse("You're looking at question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
