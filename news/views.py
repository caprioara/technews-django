from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import SubCat
from cat.models import Cat



def news_detail(request, word):

	template_name = "front/news_detail.html"

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	news = News.objects.filter(name=word)
	site = Main.objects.get(pk=2)

	context = {'news':news, 'site':site}

	return render(request, template_name, context)

def news_list(request):

	template_name = "back/news_list.html"

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	news = News.objects.all()

	context = { 'news':news }

	return render(request, template_name, context)


def news_add(request):

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	# now = datetime.datetime.now() - datetime.timedelta(days=10)
	now = datetime.datetime.now()

	ora = now.hour
	min = now.minute

	if len(str(ora)) == 1:
		ora = "0" + str(ora)
	if len(str(min)) == 1:
		min = "0" + str(min)

	time = str(ora) + ":" + str(min)

	year = now.year
	month = now.month
	day = now.day

	if len(str(day)) == 1:
		day = "0" + str(day)
	if len(str(month)) == 1:
		month = "0" + str(month)

	today = str(year) + "/" + str(month) + "/" + str(day)

	cat = SubCat.objects.all()

	template_name = "back/news_add.html"
	template_name_error = "back/error.html"

	if request.method == "POST":

		newstitle = request.POST.get('newstitle_name')
		newscat = request.POST.get('newscat_name')
		newstxtshort = request.POST.get('newstxtshort_name')
		newstxtbody = request.POST.get('newstxtbody_name')
		newsid = request.POST.get('newscat_name')

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

					newsname = SubCat.objects.get(pk=newsid).name
					ocatid = SubCat.objects.get(pk=newsid).catid

					obj = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxtbody, date=today, time=time, imageName=filename, imageUrl=url, writer="-", category=newsname, category_id=newsid, views=0, ocategory_id=ocatid)
					obj.save()

					count = len(News.objects.filter(ocategory_id=ocatid))
					obj = Cat.objects.get(pk=ocatid)
					obj.count = count
					obj.save()

					return redirect('news_list')

				else: 
					
					fs = FileSystemStorage()
					fs.delete(filename)

					error = "Your Files Is Bigger Than 8 MB"
					return render(request, template_name_error)

			else:
				fs = FileSystemStorage()
				fs.delete(filename)

				error = "Your File Not Supported"
				return render(request, template_name_error, {'error': error})

		except:

			error = "Please imput your image"
			return render(request, template_name_error, {'error': error})

	context = {'cat':cat}

	return render(request, template_name, context)

def news_delete(request, pk):

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	try: 

		obj = News.objects.get(pk=pk)

		fs = FileSystemStorage()
		fs.delete(obj.imageName)

		ocatid = News.objects.get(pk=pk).ocategory_id

		obj.delete()

		count = len(News.objects.filter(ocategory_id=ocatid))

		m = Cat.objects.get(pk=ocatid)
		m.count = count
		m.save()


	except:

		error = "Something Wrong"
		return render(request, template_name_error, {'error': error})

	return redirect('news_list')

def news_edit(request, pk):

	# login check start
	if not request.user.is_authenticated:
		return redirect('mylogin')
	# login check end

	template_name = "back/news_edit.html"
	template_name_error = "back/error.html"
	
	if len(News.objects.filter(pk=pk)) == 0:
		error = "News Not Found"
		return render(request, template_name_error, {'error': error})


	news = News.objects.get(pk=pk)
	cat = SubCat.objects.all()

	if request.method == "POST":

		newstitle = request.POST.get('newstitle_name')
		newscat = request.POST.get('newscat_name')
		newstxtshort = request.POST.get('newstxtshort_name')
		newstxtbody = request.POST.get('newstxtbody_name')
		newsid = request.POST.get('newscat_name')

		if newstitle == "" or newscat == "" or newstxtshort == "" or newstxtbody == "":
			error = "All Fields Required"
			return render(request, template_name_error, {'error': error})

		try:
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			url = fs.url(filename)

			if str(myfile.content_type).startswith('image'):

				if myfile.size < 8000000:

					newsname = SubCat.objects.get(pk=newsid).name

					obj = News.objects.get(pk=pk)

					fss = FileSystemStorage()
					fss.delete(obj.imageName)

					obj.name = newstitle
					obj.short_txt = newstxtshort
					obj.body_txt = newstxtbody
					obj.imageName = filename
					obj.imageUrl = url
					obj.catname = newscat
					obj.catid = newsid

					obj.save()
					return redirect('news_list')


				else: 
					
					fs = FileSystemStorage()
					fs.delete(filename)

					error = "Your Files Is Bigger Than 8 MB"
					return render(request, template_name_error)

			else:
				fs = FileSystemStorage()
				fs.delete(filename)

				error = "Your File Not Supported"
				return render(request, template_name_error, {'error': error})

		except:

			newsname = SubCat.objects.get(pk=newsid).name

			obj = News.objects.get(pk=pk)


			obj.name = newstitle
			obj.short_txt = newstxtshort
			obj.body_txt = newstxtbody
			obj.catname = newscat
			obj.catid = newsid

			obj.save()
			return redirect('news_list')

	context = {'pk':pk, 'news':news, 'cat':cat }

	return render(request, template_name, context)






