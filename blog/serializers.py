from rest_framework import serializers
from .models import Blog  

class BlogSerializer(serializers.ModelSerializer):
	image=serializers.ImageField(
		max_length=None, use_url=True,required=False
		)
	user=serializers.StringRelatedField()
	small_date=serializers.SerializerMethodField()

	def get_small_date(self,obj):
		return obj.date.strftime("%y-%m")

	class Meta:
		model=Blog  
		fields=['id','title','image','user','description','small_date']