from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat

def cat_list(request): 

	template_name = "back/cat_list.html"

	cat = Cat.objects.all()

	context = {'cat':cat}

	return render(request, template_name, context)