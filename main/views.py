from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):

	template_name = "front/home.html"

	site = Main.objects.get(pk=2)

	context = {'site':site}

	return render(request, template_name, context)


def about(request):

	template_name = "front/about.html"

	site = Main.objects.get(pk=2)

	context = {'site':site}

	return render(request, template_name, context)


	# site = Main.objects.get(pk=2).name
	# sitename = site.name + " | Home"