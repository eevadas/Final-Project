from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Blogs(models.Model):
	title=models.CharField(max_length=200)
	description=models.TextField()
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blogsDetail',kwargs={'pk':self.pk})

class Starred(models.Model):
	blog=models.ForeignKey(Blogs,on_delete=models.CASCADE)
	person=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.person} starred post \'{self.blog}\' '
