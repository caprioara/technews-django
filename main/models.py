from __future__ import unicode_literals
from django.db import models

class Main(models.Model):
	name = models.CharField(max_length=50)
	about = models.TextField()

	fb = models.CharField(max_length=50)
	tw = models.CharField(max_length=50)
	yt = models.CharField(max_length=50)

	tell = models.CharField(max_length=30)
	link = models.CharField(max_length=90)

	set_name = models.CharField(max_length=50)

	def __str__(self):
		return self.set_name + " | " + str(self.pk)
