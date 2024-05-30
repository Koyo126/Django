"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
		#ルートのURLconfに polls.urls モジュールの記述を反映
		#path() 関数は4つの引数を受け取ります。引数のうち route と view の2つは必須
    # route  --- URL パターンを含む文字列 
    # view   --- jango がマッチする正規表現を見つけると、 Django は指定されたビュー関数を呼び出します。
		# kwargs --- 任意のキーワード引数を辞書として対象のビューに渡せます。
		# name   --- URL に名前付けをしておけば Django のどこからでも明確に参照でき、とくにテンプレートの中で有効
		#path("polls/", include("polls.urls")),  #http://localhost:8000/polls/
    path("polls/", include("django_polls.urls")),

    path('admin/', admin.site.urls),

    path("__debug__/", include("debug_toolbar.urls")),  #https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
]
