from rest_framework import serializers
from .models import Reviews
from shop.models import OrderItem


class ReviewSerializer(serializers.ModelSerializer):
	orderItem=serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all())
	reviewed=serializers.BooleanField(required=False)

	class Meta:
		model=Reviews
		fields=["orderItem","reviewed","rating"]