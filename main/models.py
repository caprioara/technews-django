from __future__ import unicode_literals
from django.db import models

class Main(models.Model):
	name = models.TextField()
	about = models.TextField()
	fb = models.TextField(default=" ")
	tw = models.TextField(default=" ")
	yt = models.TextField(default=" ")

	set_name = models.TextField(default=" ")

	def __str__(self):
		return self.set_name + " | " + str(self.pk)
