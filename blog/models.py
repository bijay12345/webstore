from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	title=models.CharField(max_length=100)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	description=models.TextField()
	image=models.ImageField(upload_to="blog")
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} by {self.user.username}"
