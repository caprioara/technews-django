from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News


def home(request):

	template_name = "front/home.html"

	site = Main.objects.get(pk=2)
	news = News.objects.all()

	context = {'site':site, 'news':news}

	return render(request, template_name, context)


def about(request):

	template_name = "front/about.html"

	site = Main.objects.get(pk=2)

	context = {'site':site}

	return render(request, template_name, context)

def panel(request):

	template_name = "back/home.html"

	return render(request, template_name)




	# site = Main.objects.get(pk=2).name
	# sitename = site.name + " | Home"

