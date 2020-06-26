from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat

def subcat_list(request): 

	template_name = "back/subcat_list.html"

	subcat = SubCat.objects.all()

	context = {'subcat':subcat}

	return render(request, template_name, context)


def subcat_add(request): 

	template_name = "back/subcat_add.html"
	template_name_error = "back/error.html"

	if request.method == 'POST':

		name = request.POST.get('name') # name -> name field

		if name == "":

			error = "All Fields Requirded"
			return render(request, template_name_error, {'error': error})

		if len(SubCat.objects.filter(name=name)) != 0:

			error = "This Name Used Before"
			return render(request, template_name_error, {'error': error})




	return render(request, template_name)