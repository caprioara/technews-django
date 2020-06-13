from django.shortcuts import render, get_object_or_404, redirect
from .models import News

def news_detail(request, pk):

	template_name = "front/news_detail.html"

	news = News.objects.filter(pk=pk)

	context = {'news':news}

	return render(request, template_name, context)