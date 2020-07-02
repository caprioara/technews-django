from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat


def home(request):

	template_name = "front/home.html"

	site = Main.objects.get(pk=2)
	news = News.objects.all().order_by('-pk')
	cat = Cat.objects.all()
	subcat = SubCat.objects.all()
	lastnews = News.objects.all().order_by('-pk')[:3]

	context = {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews}

	return render(request, template_name, context)


def about(request):

	template_name = "front/about.html"

	site = Main.objects.get(pk=2)

	context = {'site':site}

	return render(request, template_name, context)

def panel(request):

	template_name = "back/home.html"

	return render(request, template_name)

def my_login(request):



	return render(request, 'front/login.html')




	# site = Main.objects.get(pk=2).name
	# sitename = site.name + " | Home"

