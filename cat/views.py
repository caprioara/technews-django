from django.shortcuts import render, get_object_or_404, redirect
from .models import Cat

def cat_list(request): 

	template_name = "back/cat_list.html"

	cat = Cat.objects.all()

	context = {'cat':cat}

	return render(request, template_name, context)


def cat_add(request): 

	template_name = "back/cat_add.html"
	template_name_error = "back/error.html"

	if request.method == 'POST':

		name = request.POST.get('name') # name -> name field

		if name == "":

			error = "All Fields Requirded"
			return render(request, template_name_error, {'error': error})

		if len(Cat.objects.filter(name=name)) != 0:

			error = "This Name Used Before"
			return render(request, template_name_error, {'error': error})


		b = Cat(name=name)
		b.save()

		return redirect('cat_list')

	return render(request, template_name)