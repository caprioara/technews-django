from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage


def news_detail(request, word):

	template_name = "front/news_detail.html"

	news = News.objects.filter(name=word)
	site = Main.objects.get(pk=2)

	context = {'news':news, 'site':site}

	return render(request, template_name, context)

def news_list(request):

	template_name = "back/news_list.html"

	news = News.objects.all()

	context = { 'news':news }

	return render(request, template_name, context)


def news_add(request):

	template_name = "back/news_add.html"
	template_name_error = "back/error.html"

	if request.method == "POST":

		newstitle = request.POST.get('newstitle_name')
		newscat = request.POST.get('newscat_name')
		newstxtshort = request.POST.get('newstxtshort_name')
		newstxtbody = request.POST.get('newstxtbody_name')

		if newstitle == "" or newscat == "" or newstxtshort == "" or newstxtbody == "":
			error = "All Fields Required"
			return render(request, template_name_error, {'error':error})

		try:
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)

			if str(myfile.content_type).startswith('image'):

				if myfile.size < 8000000:

					obj = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxtbody, date="2019/03/03", imageName=filename, imageUrl=url, writer=" ", category=newscat, category_id=0, views=0)
					obj.save()
					return redirect('news_list')

				else: 

					error = "Your Files Is Bigger Than 8 MB"
					return render(request, template_name_error)

			else:

				error = "Your File Not Supported"
				return render(request, template_name_error, {'error': error})

		except:

			error = "Please imput your image"
			return render(request, template_name_error, {'error': error})

	return render(request, template_name)







