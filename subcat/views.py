from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCat
from cat.models import Cat

def subcat_list(request): 

	template_name = "back/subcat_list.html"

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	subcat = SubCat.objects.all()

	context = {'subcat':subcat}

	return render(request, template_name, context)


def subcat_add(request): 

	template_name = "back/subcat_add.html"
	template_name_error = "back/error.html"

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	cat = Cat.objects.all()

	if request.method == 'POST':

		name = request.POST.get('name') # name -> name field
		catid = request.POST.get('cat')

		if name == "":

			error = "All Fields Requirded"
			return render(request, template_name_error, {'error': error})

		if len(SubCat.objects.filter(name=name)) != 0:

			error = "This Name Used Before"
			return render(request, template_name_error, {'error': error})

		catname = Cat.objects.get(pk=catid).name

		b = SubCat(name=name, catname = catname, catid=catid)
		b.save()
		return redirect('subcat_list')

	context = {'cat':cat}

	return render(request, template_name,context)