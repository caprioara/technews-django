from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
	template_name = "front/home.html"
	return render(request, template_name)


def about(request):
	template_name = "front/about.html"
	return render(request, template_name)

