from rest_framework import serializers
from .models import Items,Order,OrderItem,BillingAddress
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
	image=serializers.ImageField(
            max_length=None, use_url=True,required=False
        )
	image2=serializers.ImageField(
            max_length=None, use_url=True,required=False
        )

	image3=serializers.ImageField(
		max_length=None, use_url=True,required=False
		)
	image4=serializers.ImageField(
		max_length=None, use_url=True,required=False
		)
	likers=serializers.StringRelatedField(many=True,read_only=True)
	class Meta:
		model=Items  
		fields = ["id","name","company","description","likers","price","image","image2","image3","image4"]


class OrderItemSerializer(serializers.ModelSerializer):
	item=serializers.PrimaryKeyRelatedField(queryset=Items.objects.all())
	dateadded=serializers.DateField()
	user=serializers.StringRelatedField()

	def get_total_price(self,obj):
		return obj.quantity*obj.item.price

	class Meta:
		model=OrderItem
		fields=['id','item','dateadded',"size_choices",'quantity','user']


class OrderSerializer(serializers.ModelSerializer):
	item=serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all())
	user=serializers.StringRelatedField()
	order_date=serializers.SerializerMethodField()
	final_price=serializers.SerializerMethodField()

	def get_order_date(self,obj):
		return obj.ordered_date

	def get_final_price(self,obj):
		total=0 
		for order_items in obj.item.all():
			total+=order_items.get_total_price()
		return total

	class Meta:
		model=Order  
		fields=["id","item","user","order_date", "final_price","ordered","billing_address","payment"]

class BillingSerializer(serializers.ModelSerializer):
	user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	class Meta:
		model=BillingAddress
		fields=['user','primaryNumber','secondaryNumber','street','address','pincode','city','state']

class LikeSerializer(serializers.ModelSerializer):
	likers=serializers.StringRelatedField(many=True,read_only=True)
	class Meta:
		model=Items 
		fields=["likers"]