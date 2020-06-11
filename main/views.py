from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):

	template_name = "front/home.html"
	sitename = "Django | Home"
	context = {'sitename':sitename, 'site':site}

	site = Main.object.filter(pk=1)

	return render(request, template_name, context)


def about(request):

	template_name = "front/about.html"
	sitename = "Django | About"
	context = {'sitename':sitename}
	return render(request, template_name, context)

