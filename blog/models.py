from django.db import models
from datetime import date

# Create your models here.
class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField(auto_now=False,auto_now_add=True)
	body = models.TextField()
	image = models.ImageField(upload_to='images')

	def summary(self):
		return self.body[:100] + '...'

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')


	def __str__(self):
		return self.title