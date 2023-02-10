from django.shortcuts import render,get_object_or_404,redirect
from .models import Items,Logo,Buttons,Features,Banner,Blog,\
AboutItems,FeedBack,OrderItem,Order,BillingAddress,Payment,Rating
from django.contrib.auth.decorators import login_required
from datetime import date
from rest_framework.views import APIView
from .serializers import ItemSerializer,OrderSerializer,BillingSerializer,LikeSerializer,RatingSerializer,ContactSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from django.core.paginator import Paginator


@login_required
def home(request):
	items=Items.objects.all()

	logo=Logo.objects.get(id=1)
	button=Buttons.objects.get(id=1)
	features=Features.objects.all()
	repairbanner=Banner.objects.get(name="repair")

	context={
	"items":items,
	"logo":logo,
	"button":button,
	"features":features,
	"repairbanner":repairbanner,
	"h_status":"active"
	}

	print(request.GET.get("page"))

	return render(request,"shop/home.html",context)


@login_required
def productDetail(request,id):
	product=Items.objects.get(id=id)
	return render(request,"shop/productdetail.html",{"product":product,"pd_status":"active"})


def about(request):
	feature=Features.objects.all()
	items=AboutItems.objects.get(id=1)
	context={
	"features":feature,
	"items":items,
	"ab_active":"active"
	}
	return render(request,"shop/about.html",context)

def contact(request):
	feedbacks=FeedBack.objects.all()
	return render(request,"shop/contact.html",{'feedbacks':feedbacks,"con_status":"active"})


@login_required
def add_to_cart(request,id):
	item=get_object_or_404(Items,id=id)
	order_item,created=OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
	order_qs=Order.objects.filter(user=request.user,ordered=False)

	data=dict(request.POST.items())
	size=data.get("choice")

	if order_qs.exists():
		order=order_qs[0]
		if order.item.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
		else:
			if size != "None":
				order_item.size=size
				order_item.save()
			order.item.add(order_item)
	else:
		order=Order.objects.create(user=request.user)
		if size != "None":
			order_item.size=size
			order_item.save()

		order.item.add(order_item)
	return redirect("cart")


@login_required
def remove_from_cart(request,id):
	item=get_object_or_404(Items,id=id)
	order_qs=Order.objects.filter(user=request.user,ordered=False)

	if order_qs.exists():
		order=order_qs[0]

		if order.item.filter(item__id=item.id).exists():
			order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
			order.item.remove(order_item)
			return redirect("cart")
		else:
			return redirect("cart")
	else:
		return redirect("cart")


@login_required
def remove_single_item_from_cart(request,id):
	item=get_object_or_404(Items,id=id)
	order_qs=Order.objects.filter(user=request.user,ordered=False)

	if order_qs.exists():
		order=order_qs[0]

		if order.item.filter(item__id=item.id).exists():
			order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order.item.remove(order_item)
			
			return redirect("cart")
		else:
			return redirect("cart")
	else:
		return redirect("cart")


# @login_required
# def checkout(request):
# 	if request.method == "POST":
# 		data=dict(request.POST.items())
# 		print(data)
# 		phonenumber = data.get('phone')
# 		secondary_number = data.get('sec_number')
# 		street = data.get('street')
# 		address = data.get('address')
# 		pin = data.get('pin')
# 		city = data.get('city')
# 		state = data.get('state')
# 		user=request.user  
# 		payment_options=data.get('payment')

# 		print(user,phonenumber,secondary_number,street,address,pin,city,state)

# 		billing_address=BillingAddress(
# 			user=user,
# 			primaryNumber=phonenumber,
# 			secondaryNumber=secondary_number,
# 			street=street,
# 			address=address,
# 			pincode=pin,
# 			city=city,
# 			state=state
# 			)
# 		try:
# 			order=Order.objects.get(user=request.user,ordered=False)
# 		except ObjectDoesNotExist:
# 			messages.info(request,"You do not have an active order")
# 			return redirect("shop")

# 		payment=Payment(cash_on_delivery=payment_options,user=user)
# 		billing_address.save()
# 		payment.save()
# 		order.billing_address = billing_address
# 		order.ordered=True
# 		order.save()
# 		messages.success(request,"Order Successful")
# 		return redirect("shop")

# 	orders=Order.objects.get(user=request.user)
# 	return render(request,"shop/checkout.html",{"orders":orders})



def orderDetail(request,id):
	item=OrderItem.objects.get(id=id)
	items=Items.objects.all()

	order=Order.objects.get(item=item,ordered=True,user=request.user)

	rated=False
	if Rating.objects.filter(user=request.user,item=item.item.id).exists():
		rated=True

	return render(request,"shop/orderdetail.html",{"product":item,"items":items,"order":order,"rated":rated})


# -------------------------------------------            API DEPLOYMENT            ---------------------------------------------------


class HomeApiView(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	def get(self,request,id=None,format=None):
		if id is not None:
			item=Items.objects.get(id=id)
			serializer=ItemSerializer(item)
			return Response({"product":serializer.data},template_name="shop/productdetail.html")
		items=Items.objects.all()
		serializer=ItemSerializer(many=True)
		return Response({"items":serializer.data},template_name="shop/home.html")



class ShopApiView(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	def get(self,request,format=None):
		items=Items.objects.all()
		serializer=ItemSerializer(items,many=True)
		item=serializer.data 

		paginator=Paginator(serializer.data,40)
		page_number = request.GET.get('page')
		page_obj=paginator.get_page(page_number)

		return Response({"items":page_obj,"s_status":"active"},template_name="shop/shop.html")

	def post(self,request,format=None):
		category=dict(request.POST.items()).get("choice")
		items=Items.objects.all().filter(category_choices=category)
		serializer=ItemSerializer(items,many=True)
		return Response({"items":serializer.data,"s_status":"active"},template_name="shop/shop.html")


class CartApi(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	template_name="shop/cart.html"
	def get(self,request,format=None):
		try:
			orders=Order.objects.get(user=self.request.user,ordered=False)
			serializer=OrderSerializer(orders)
			return Response({"orders":serializer.data})
		except ObjectDoesNotExist:
			messages.info(request,"You do not have an active order")
			return Response({"empty":"empty"})




class CheckoutView(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	def get(self,request,format=None):
		orders=Order.objects.get(user=request.user,ordered=False)
		serializer=OrderSerializer(orders)
		return Response({"orders":serializer.data},template_name="shop/checkout.html")

	def post(self,request,format=None):
		data=dict(request.POST.items())

		phonenumber = data.get('phone')
		secondary_number = data.get('sec_number')
		street = data.get('street')
		address = data.get('address')
		pin = data.get('pin')
		city = data.get('city')
		state = data.get('state')
		user=request.user.id
		payment_options=data.get('payment')

		data1=dict(
			user=user,
			primaryNumber=phonenumber,
			secondaryNumber=secondary_number,
			street=street,
			address=address,
			pincode=pin,
			city=city,
			state=state
			)
		order=Order.objects.get(user=request.user,ordered=False)

		orderitems=order.item.all()
		orderitems.update(ordered=True)
		for item in orderitems:
			item.save()


		billingserializer=BillingSerializer(data=data1)
		if billingserializer.is_valid():
			billingserializer.save()

		billing=BillingAddress.objects.order_by("user","-id")[0]

		order.billing_address=billing
		order.ordered=True
		order.save()

		messages.success(request,"Successfully placed your order")
		
		return redirect("shop")


class LikeView(APIView):
	def post(self,request,format=None):
		data=dict(request.POST.items())
		itemId=data['itemId']
		item=get_object_or_404(Items,id=itemId)
		data={
		"likers":request.user.id
		}
		serializer=LikeSerializer(item,data=data,partial=True)
		if item.likers.filter(id=request.user.id).exists():
			if serializer.is_valid(raise_exception=True):
				item.likers.remove(request.user)
				return redirect("shop")
		else:
			if serializer.is_valid(raise_exception=True):
				item.likers.add(request.user)
				return redirect("shop")


class RatingView(APIView):
	def post(self,request,id,format=None):
		d=request.data
		rating=d["star"]
		item_id=d['item_id']
		user=request.user
		item=get_object_or_404(Items,id=item_id)
		data_={
		"rating":rating,
		"user":user.id,
		"item":item.id,
		}

		serializer=RatingSerializer(data=data_)


		if serializer.is_valid(raise_exception=True):
			serializer.save()
			messages.success(request,f"Thank you for your valuable rating")
			return redirect("orderDetail",id=id)
		else:
			messages.warning(request,f"please rate correctly")
			return redirect("orderDetail",id=id)
		return redirect("orderDetail",id=id)


class ContactApiView(APIView):
	renderer_classes=[TemplateHTMLRenderer]
	def post(self,request,format=None):
		data=request.POST  
		serializer=ContactSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			messages.success(request,"Your query has reached us, We'll soon get back to you.")
		else:
			messages.error(request,"Please fill the form correctly")
			return redirect("contact")
		return redirect("contact")