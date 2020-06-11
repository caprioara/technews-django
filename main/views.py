from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


def home(request):
	template_name = "home.html"
	return render(request, template_name)


