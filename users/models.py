from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from shop.models import OrderItem
from django.contrib.auth.models import User

class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="profilepics",default="defaultuser.jpeg")

	def __str__(self):
		return self.user.username


