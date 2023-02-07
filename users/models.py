from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from shop.models import OrderItem


class Profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="profilepics",default="defaultuser.jpeg")

	def __str__(self):
		return self.user.username


class Reviews(models.Model):
	rating=models.IntegerField(validators=[MaxValueValidator(5)])
	reviewed=models.BooleanField(default=False)
	orderItem=models.ForeignKey(OrderItem,on_delete=models.CASCADE,blank=True,null=True)	


	def __str__(self):
		return f"{self.rating} star rating"
