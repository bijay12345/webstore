from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


CATEGORY_CHOICES=(
	('DF','None'),
	('GL','goggles'),
	('S','Shirts'),
	('PN','Pants'),
	('SK','Skirts'),
	('SH','Shoes')
	)



class Items(models.Model):
	name=models.CharField(max_length=100)
	category_choices=models.CharField(max_length=5, choices=CATEGORY_CHOICES)
	company=models.CharField(max_length=100)
	description=models.CharField(max_length=300)
	price=models.DecimalField(decimal_places=2,max_digits=8)
	likers=models.ManyToManyField(User,related_name="likers",blank=True)
	image=models.ImageField(upload_to="products",default="default.jpg")
	image2=models.ImageField(upload_to="products",default="default.jpg")
	image3=models.ImageField(upload_to="products",default="default.jpg")
	image4=models.ImageField(upload_to="products",default="default.jpg")

	def __str__(self):
		return f"{self.name} from {self.company}"


class OrderItem(models.Model):
	item=models.ForeignKey(Items,on_delete=models.CASCADE)
	dateadded=models.DateField(auto_now_add=True)
	quantity=models.IntegerField(default=1)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	ordered=models.BooleanField(default=False)
	size=models.CharField(max_length=5,default="M")

	def __str__(self):
		return f"{self.quantity} of {self.item.name}"

	def get_total_price(self):
		return self.quantity*self.item.price


class Order(models.Model):
	item=models.ManyToManyField(OrderItem,related_name="orders")
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	ordered_date=models.DateField(auto_now_add=True)
	ordered=models.BooleanField(default=False)
	billing_address=models.ForeignKey("BillingAddress",on_delete=models.SET_NULL,blank=True,null=True)
	payment=models.ForeignKey("Payment",on_delete=models.SET_NULL,blank=True,null=True)


	def __str__(self):
		return f"{self.user.username}'s order"


	def get_final_price(self):
		total=0 
		for order_items in self.item.all():
			total+=order_items.get_total_price()
		return total




class BillingAddress(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	primaryNumber=models.CharField(max_length=10)
	secondaryNumber=models.CharField(max_length=10)
	street=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	pincode=models.CharField(max_length=10)
	city=models.CharField(max_length=100)
	state=models.CharField(max_length=100)

	def __str__(self):
		return f"{self.user.username}'s billing address"



class Payment(models.Model):
	cash_on_delivery=models.BooleanField(default=False)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.username}'s payment"





class HomeBanner(models.Model):
	heading=models.CharField(max_length=100)
	heading2=models.CharField(max_length=100)
	bulletPoint=models.CharField(max_length=100)
	paragraph=models.CharField(max_length=200)


	def __str__(self):
		return f"{self.heading} 'heading of id no.'{self.id}"	


class Features(models.Model):
	featuretext=models.CharField(max_length=100)
	images=models.ImageField(upload_to="features")

	def __str__(self):
		return self.featuretext

class Blog(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	images=models.ImageField(upload_to="blog")

class Banner(models.Model):
	name=models.CharField(max_length=100)
	images=models.ImageField(upload_to="banner")

class FooterInfos(models.Model):
	name=models.CharField(max_length=100)
	image=models.ImageField(upload_to="footer")


class AboutItems(models.Model):
	aboutheader = models.CharField(max_length=100)
	aboutheaderparagraph=models.CharField(max_length=200)
	aboutimage=models.ImageField(upload_to="about")
	aboutVideo=models.FileField(upload_to="videos",null=True,blank=True)

	def __str__(self):
		return f"about-info no. {self.id}"

class Logo(models.Model):
	image=models.ImageField(upload_to="logos")

class Buttons(models.Model):
	button=models.ImageField(upload_to="bottons")

class FeedBack(models.Model):
	name=models.CharField(max_length=100)
	designation=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	phone=models.CharField(max_length=12)
	image=models.ImageField(upload_to="feedbacks")

	def __str__(self):
		return self.name


class Rating(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	item=models.ForeignKey(Items,on_delete=models.CASCADE)
	rating=models.IntegerField(validators=[MaxValueValidator(5)])

	def __str__(self):
		return self.user.username

class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	subject=models.CharField(max_length=1000)
	message=models.TextField()
	
	def __str__(self):
		return f"{self.name}'s message"