from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main

def news_detail(request, word):

	template_name = "front/news_detail.html"

	news = News.objects.filter(name=word)
	site = Main.objects.get(pk=2)

	context = {'news':news, 'site':site}

	return render(request, template_name, context)

def news_list(request):

	template_name = "back/news_list.html"

	news = News.objects.all()

	context = { 'news':news }

	return render(request, template_name, context)


def news_add(request):

	template_name = "back/news_add.html"

	news = News.objects.all()

	context = { 'news':news }

	return render(request, template_name, context)