from __future__ import unicode_literals
from django.db import models

class News(models.Model):

	name = models.CharField(max_length=50)
	short_txt = models.TextField()
	body_txt = models.TextField()
	date = models.CharField(max_length=12)
	time = models.CharField(max_length=12, default="00:00")
	imageName = models.TextField()
	imageUrl = models.TextField(default=" ")
	writer = models.CharField(max_length=50)
	category = models.CharField(max_length=50, default="-")
	category_id = models.IntegerField(default=0)
	ocategory_id = models.IntegerField(default=0)
	views = models.IntegerField(default=0)

	def __str__(self):
		return self.name
