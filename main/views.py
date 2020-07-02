from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import SubCat
from django.contrib.auth import authenticate, login, logout


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

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	return render(request, template_name)

def mylogin(request):

	if request.method == 'POST':

		uuser = request.POST.get('username')
		upass = request.POST.get('password')

		if uuser != "" and upass != "":

			user = authenticate(username = uuser, password = upass)

			if user != None:

				login(request, user)
				return redirect('panel')


	return render(request, 'front/login.html')

def mylogout(request):

	logout(request)

	return redirect('mylogin')


	# site = Main.objects.get(pk=2).name
	# sitename = site.name + " | Home"

