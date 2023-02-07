from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
from .models import Profile,Reviews
from shop.models import Order,Items,OrderItem
from .serializers import ReviewSerializer
from rest_framework.views import APIView

def register(request):
	if request.method == "POST":
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")
	else:
		form=UserRegistrationForm()

	return render(request,"users/register.html",{"form":form})


def profile(request):
	if request.method == "POST":
		u_form=UserUpdateForm(request.POST,instance=request.user)
		p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect("profile")
	else:
		u_form=UserUpdateForm(instance=request.user)
		p_form=ProfileUpdateForm()

	orders=Order.objects.filter(user=request.user,ordered=True)
	likedProducts=Items.objects.filter(likers=request.user.id)
	
	ratings=Reviews.objects.filter(reviewed=True)

	return render(request,"users/profile.html",{"u_form":u_form,"p_form":p_form,"profile_status":"active","orders":orders,"likedProducts":likedProducts,"ratings":ratings})




class ReviewApi(APIView):
	def post(self,request,format=None):
		data=dict(request.POST.items())

		rating=data["star"]
		item_id=data["item_id"]

		data={
		"rating":rating,
		"reviewed":"True",
		"orderItem":item_id,
		}

		serializer= ReviewSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return redirect("orderDetail", id=item_id)
		else:

			print(serializer.errors)
		return redirect("orderDetail", id=item_id)

