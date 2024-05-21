from django.shortcuts import render
from django.views import View

# Create your views here.
class SampleView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'app_folder/top_page.html')
top_page = SampleView.as_view()
